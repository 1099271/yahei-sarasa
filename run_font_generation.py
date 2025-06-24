import sys
import generate_fonts as gen

if __name__ == '__main__':
    task = sys.argv[1]
    if task == 'regular':
        gen.gen_regular()
    elif task == 'bold':
        gen.gen_bold()
    elif task == 'light':
        gen.gen_light()
    else:
        raise ValueError('Unknown task: ' + task) 