import hashlib
from pydantic import BaseModel

class VibeResult(BaseModel):
    score: int
    message: str
    color_class: str

def calculate_vibe(name: str, emoji: str) -> VibeResult:
    # Deterministic hash based on name + emoji
    input_str = f"{name.lower().strip()}{emoji}"
    hash_obj = hashlib.sha256(input_str.encode())
    # Convert first byte to 0-100 score
    score = int(hash_obj.hexdigest(), 16) % 101

    if score > 90:
        msg = "LEGENDARY VIBES. You radiate pure Solarized Yellow energy."
        color = "text-solarized-yellow"
    elif score > 75:
        msg = "Immaculate vibes. Like a well-configured neovim setup."
        color = "text-solarized-green"
    elif score > 50:
        msg = "Solid vibes. You get the job done, no fuss."
        color = "text-solarized-cyan"
    elif score > 30:
        msg = "Meh. Your vibes are deprecated."
        color = "text-solarized-violet"
    elif score > 10:
        msg = "Yikes. Try restarting your router."
        color = "text-solarized-orange"
    else:
        msg = "VIBE CHECK FAILED. Segfault immediately."
        color = "text-solarized-red"

    return VibeResult(score=score, message=msg, color_class=color)
