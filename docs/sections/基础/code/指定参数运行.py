import sys

def main():
    init_param = sys.argv[1] if len(sys.argv) > 1 else 'default'
    local_flag = '--local' in sys.argv

    print(f"Initialization parameter: {init_param}")
    if local_flag:
        print("Running in local mode.")

if __name__ == '__main__':
    main()