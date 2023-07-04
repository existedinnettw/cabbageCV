
'''
this file is no longer need, already someone done this process.
'''


import os
import random
import math
import copy
import shutil

def random_split_data(path:str, out_path:str, img_type:str="jpg", annotate_type:str="txt", split_pct:list=[0.7,0.1,0.2]):
    '''
    random select and copy file and annotate to out_path

    example
    ```python
    data_util.random_split_data("../obj/", "../CABBAGE.v1/")
    ```

    param
    ---
    path:str
        path to all the image and tags.
    out_path:str
        output path to `train/` `valid/` `test/`

    todo
    ---
    should path be list of path?
    '''
    # delte path and remake one
    if (not math.isclose(sum(split_pct),1.0)) or len(split_pct)!=3:
        #assert split_pct
        print(sum(split_pct))
        raise ValueError("split_pct error")
    
    #clean and recreate target folder
    sub_dirs=['train', 'valid', 'test']
    for sub_dir in sub_dirs:
        full_sub_dir=os.path.join(out_path, sub_dir)
        shutil.rmtree(full_sub_dir, ignore_errors=True)
        print(full_sub_dir)
        os.makedirs(full_sub_dir, exist_ok=True)


    # start handle path & image
    all_path=set(os.listdir(path))
    img_path=set([i for i in all_path if img_type in i])

    remain_img_path=copy.deepcopy(img_path)
    # print(len(remain_img_path))

    train_img_path=set(random.sample(remain_img_path,int(len(img_path)*split_pct[0])))
    remain_img_path-=train_img_path
    train_img_path=list(train_img_path)
    # print(len(remain_img_path))
    

    test_img_path=set(random.sample(remain_img_path,int(len(img_path)*split_pct[2])))
    remain_img_path-=test_img_path
    test_img_path=list(test_img_path)
    # print(len(remain_img_path))


    valid_img_path=list(remain_img_path)

    # print(len(train_img_path), len(valid_img_path), len(test_img_path), len(img_path) )

    # copy files
    for sub_dir, sub_img_path in zip(sub_dirs,[train_img_path,valid_img_path,test_img_path]):
        def copy_elm(x):
            img_src=os.path.join(path,x)
            # print(src, out_path)
            shutil.copy(img_src, os.path.join(out_path,sub_dir)) #copy img
            annotate_src=os.path.splitext(img_src)[0]+'.'+annotate_type
            shutil.copy(annotate_src, os.path.join(out_path,sub_dir))#copy annotate
        list(map( copy_elm, sub_img_path))


    # print(img_path)

from sahi.utils.coco import Coco, CocoCategory, CocoImage, CocoAnnotation
from sahi.utils.file import save_json
from PIL import Image


def to_coco_ds(path:str, categories:list=['cabbage'], img_type:str="jpg", annotate_type:str="txt"):
    '''
    output path(annotate) is same as input path
    param
    ---
    path: str
        input path
    '''
    coco = Coco()

    for i in range(len(categories)):
        coco.add_category(CocoCategory(id=i, name=categories[i]))

    all_path=os.listdir(path)
    img_path=set([i for i in all_path if img_type in i])

    # foreach image,
    for sub_path in img_path:
        filename = os.path.join(path, sub_path)

        # print(all_path)
        width, height = Image.open(filename).size
        coco_image = CocoImage(file_name=filename, height=height, width=width)

        anno_file= os.path.join( path, os.path.splitext(filename)[0]+'.'+annotate_type)

        with open(anno_file, 'r') as f:
            lines=f.readlines()

        #readout relevant annotate and then set to coco annotate.
        #class
        for line in lines:
            bbox=line.split(' ')
            bbox=[float(i) for i in bbox][1:]
            x_min, y_min, img_width, img_height=tuple(bbox)
            x_min*=width
            y_min*=height
            img_width*=width
            img_height*=height

            coco_image.add_annotation(
                CocoAnnotation(
                    bbox=[x_min, y_min, img_width, img_height],
                    category_id=0,
                    category_name=categories[0] #we have cabbage only
                )
            )
        save_path=path
        coco.add_image(coco_image)
        save_json(data=coco.json, save_path=save_path)

    



