#!/usr/bin/env python3
import os, fnmatch


def main():
    for (root,dirs,files) in os.walk(os.getcwd(), topdown=True):
        for file in files:
            if '.mp4' not in file:
                continue
            if 'redditsave.com_' in file:
                string_list = file.split('_')
                new_string = ''
                for X in range(len(string_list)):
                    print(string_list[X])
                    if string_list[X] == 'redditsave.com':
                        continue
                    if X == 1:
                        new_string=new_string+string_list[X].capitalize()+' '
                        continue
                    new_string=new_string+string_list[X]+' '
                new_filename = new_string.split('-')
                print(new_filename)
            os.rename(file,new_filename[0]+'.mp4')


if __name__ == "__main__":main()
