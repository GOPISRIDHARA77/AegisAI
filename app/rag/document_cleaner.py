import re
def clean_text(text:str) -> str:
    #remove extra space 
    text = re.sub(r"[ \t]+", " ",text)
    # remove uncessary blank lines 
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # remove spaces at the begining/end of lines 
    text =  "\n".join(line.strip() for line in text.splitlines())

    return text.strip()