import glob
import os
import re
import shutil

if __name__ == "__main__":
    ds_path = "/home/at70870/local_scratch/Site-CBIC"
    subjects = os.listdir(ds_path)
    for sub in subjects:
        src = os.path.join(ds_path, sub, "anat")

        files = os.listdir(src)
        files = filter(lambda x: "nii.gz" in x, files)
        pattern = r"sub-.*_acq-(.*)_T1w"

        modals = []
        for f in files:
            match = re.match(pattern, f)
            modals.append(match.group(1))
        for m in modals:
            if not "Norm" in m:
                sesdir = os.path.join(ds_path, sub, f"ses-{m}", "anat")

                os.makedirs(sesdir)
                for file in glob.glob(os.path.join(src, f"*{m}_T1w*")):
                    extension = os.path.basename(file).split(".")[1:]
                    extension = ".".join(extension)
                    newname = f"{sub}_ses-{m}_T1w.{extension}"
                    final_path = os.path.join(sesdir, newname)
                    print(final_path)
                    shutil.move(file, final_path)
        if os.path.exists(src):
            shutil.rmtree(src)
