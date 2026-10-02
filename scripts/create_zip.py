import os
import zipfile

def create_project_zip():
    output_filename = "forgepoint-project.zip"
    public_output_path = os.path.join("public", output_filename)
    root_output_path = output_filename
    
    os.makedirs("public", exist_ok=True)
    
    # Exclude these directories and files
    exclude_dirs = {
        "node_modules",
        ".git",
        "dist",
        ".cache",
        "__pycache__"
    }
    exclude_files = {
        output_filename,
        "forgepoint-source.zip",
        ".DS_Store"
    }

    # Files to include
    file_list = []
    for root, dirs, files in os.walk("."):
        # modify dirs in place to skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file in exclude_files:
                continue
            if file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            # relative path without ./
            rel_path = os.path.relpath(full_path, ".")
            if rel_path.startswith("public/" + output_filename):
                continue
            file_list.append((full_path, rel_path))

    print(f"Adding {len(file_list)} files to zip...")
    with zipfile.ZipFile(public_output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for full_path, rel_path in sorted(file_list):
            zipf.write(full_path, rel_path)

    # Also copy to root for convenience
    import shutil
    shutil.copyfile(public_output_path, root_output_path)
    print(f"Successfully generated {public_output_path} ({os.path.getsize(public_output_path)} bytes) and {root_output_path}")

if __name__ == "__main__":
    create_project_zip()
