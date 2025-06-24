import sys
import generate_simsun as simsun

if __name__ == '__main__':
    task = sys.argv[1]
    if task == 'ttc':
        simsun.gen_simsun_ttc()
    elif task == 'ext':
        simsun.gen_simsun_ext()
    else:
        raise ValueError('Unknown task: ' + task) 