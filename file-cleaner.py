import os
import shutil
from pathlib import Path
from typing import List,Union

class CleanUpFiles:
    def __init__(self)-> None:
        self.BASE_DIR   : str = Path(__file__).resolve().parent.parent
        self.target_dir : str = 'utils'

    def main(self)-> None:
        file_list : List[Union[str,int]] = self.get_file_list()
        self.clean_up(file_list=file_list)

    def clean_up(self,file_list: List[Union[str,int]]):
        for file in file_list:
            filename , extension : str = os.path.splitext(file)
            if extension == '.py' :
                continue

            elif extension == '.pdf' :
                src_file = os.path.join(self.BASE_DIR , self.target_dir + '/' + file)
                dst_file = os.path.join(self.BASE_DIR , 'pdf' + '/'  + file)

                if not os.path.exists(f'{self.BASE_DIR}/pdf') :
                    os.mkdir(f'{self.BASE_DIR}/pdf')
                shutil.move(src_file , dst_file)

            elif extension == '.hwp':
                src_file = os.path.join(self.BASE_DIR , self.target_dir + '/' + file)
                dst_file = os.path.join(self.BASE_DIR , 'hwp')

                if not os.path.exists(f'{self.BASE_DIR}/hwp') :
                    os.mkdir(f'{self.BASE_DIR}/hwp')
                shutil.move(src_file , dst_file)

            elif extension == '.xlsx':
                src_file = os.path.join(self.BASE_DIR , self.target_dir + '/' + file)
                dst_file = os.path.join(self.BASE_DIR , 'xlsx')

                if not os.path.exists(f'{self.BASE_DIR}/xlsx') :
                    os.mkdir(f'{self.BASE_DIR}/xlsx')
                shutil.move(src_file , dst_file)

            elif extension == '.jpg':
                src_file = os.path.join(self.BASE_DIR , self.target_dir + '/' + file)
                dst_file = os.path.join(self.BASE_DIR , 'jpg')

                if not os.path.exists(f'{self.BASE_DIR}/jpg') :
                    os.mkdir(f'{self.BASE_DIR}/jpg')
                shutil.move(src_file , dst_file)

            elif extension == '.jpeg':
                src_file = os.path.join(self.BASE_DIR , self.target_dir + '/' + file)
                dst_file = os.path.join(self.BASE_DIR , 'jpeg')

                if not os.path.exists(f'{self.BASE_DIR}/jpeg') :
                    os.mkdir(f'{self.BASE_DIR}/jpeg')
                shutil.move(src_file , dst_file)

            elif extension == '.png':
                src_file = os.path.join(self.BASE_DIR , self.target_dir + '/' + file)
                dst_file = os.path.join(self.BASE_DIR , 'png')

                if not os.path.exists(f'{self.BASE_DIR}/png') :
                    os.mkdir(f'{self.BASE_DIR}/png')
                shutil.move(src_file , dst_file)

            else :
                src_file = os.path.join(self.BASE_DIR , self.target_dir + '/' + file)
                dst_file = os.path.join(self.BASE_DIR , 'txt')

                if not os.path.exists(f'{self.BASE_DIR}/txt') :
                    os.mkdir(f'{self.BASE_DIR}/txt')
                shutil.move(src_file , dst_file)

    def get_file_list(self)-> List[Union[str,int]]:
        target_path : str = os.path.join(self.BASE_DIR,self.target_dir)

        file_list : List[Union[str,int]] = os.listdir(target_path)
        return file_list

if __name__ == '__main__':
    app = CleanUpFiles()
    app.main()





