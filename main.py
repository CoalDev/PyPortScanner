from portScanner import portScanner

def main():
    ps = portScanner('127.0.0.1', 1, 136)
    ps.scan(clearTerminal=True)

if __name__ == "__main__":
    main()