from path import Path

if __name__ == "__main__":
    
    p = Path("my_dir")
    p.makedirs_p()

    file = p/"my_file.txt"
    file.touch()

    file.write_text("xxyyzz")
  
    print(file.read_text())
