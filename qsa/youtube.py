"""YouTube Data API v3 upload. Requires one-time OAuth (python3 -m qsa auth).

Needs: pip3 install google-api-python-client google-auth-oauthlib
Credentials: client_secret.json (OAuth Desktop client from Google Cloud
Console) in the project root; token.json is written after auth. Both are
gitignored."""
import os

from .config import project_root

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def _paths():
    root = project_root()
    return (os.path.join(root, "client_secret.json"),
            os.path.join(root, "token.json"))


def _require_google_libs():
    try:
        import googleapiclient  # noqa: F401
        import google_auth_oauthlib  # noqa: F401
    except ImportError:
        raise SystemExit(
            "Google API libraries missing. Run:\n"
            "  pip3 install google-api-python-client google-auth-oauthlib")


def run_auth_flow():
    _require_google_libs()
    from google_auth_oauthlib.flow import InstalledAppFlow
    client_secret, token_file = _paths()
    if not os.path.exists(client_secret):
        raise SystemExit(
            "client_secret.json not found in project root.\n"
            "Create an OAuth 'Desktop app' client in Google Cloud Console\n"
            "(APIs & Services > Credentials, with YouTube Data API v3 enabled)\n"
            "and save the downloaded JSON as client_secret.json here.")
    flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(token_file, "w") as fh:
        fh.write(creds.to_json())
    print("Authorised. Token saved to token.json")


def get_service():
    _require_google_libs()
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    _, token_file = _paths()
    if not os.path.exists(token_file):
        raise SystemExit("Not authorised yet. Run: python3 -m qsa auth")
    creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(token_file, "w") as fh:
                fh.write(creds.to_json())
        else:
            raise SystemExit("Token invalid. Re-run: python3 -m qsa auth")
    return build("youtube", "v3", credentials=creds)


def upload_video(service, file_path, title, description, tags,
                 category_id, privacy_status):
    from googleapiclient.http import MediaFileUpload
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    request = service.videos().insert(
        part="snippet,status", body=body, media_body=media)
    response = None
    while response is None:
        _, response = request.next_chunk()
    return response["id"]
