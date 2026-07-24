"""Render a source segment as a vertical 1080x1920 Short with ffmpeg."""
import subprocess


def render_short(src, start, end, out_path, width, height, background):
    duration = end - start
    if background == "blur":
        vf = (
            "[0:v]scale={w}:{h}:force_original_aspect_ratio=increase,"
            "crop={w}:{h},boxblur=24:6[bg];"
            "[0:v]scale={w}:-2[fg];"
            "[bg][fg]overlay=(W-w)/2:(H-h)/2[vout]"
        ).format(w=width, h=height)
    else:
        vf = (
            "[0:v]scale={w}:-2,"
            "pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:black[vout]"
        ).format(w=width, h=height)

    fade_start = max(0.0, duration - 0.4)
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", "%.3f" % start, "-t", "%.3f" % duration,
        "-i", src,
        "-filter_complex", vf,
        "-map", "[vout]", "-map", "0:a?",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
        "-r", "30", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k",
        "-af", "afade=t=out:st=%.3f:d=0.4" % fade_start,
        "-movflags", "+faststart",
        out_path,
    ]
    subprocess.run(cmd, check=True)
