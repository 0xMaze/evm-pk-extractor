from web3 import Account, Web3


class Extractor:
    def __init__(self) -> None:
        Account.enable_unaudited_hdwallet_features()

    def extract(self) -> bool:
        private_keys = []
        seed_phrases = Extractor.read_from_txt()
        for seed in seed_phrases:
            account = Web3().eth.account.from_mnemonic(mnemonic=seed)
            private_keys.append(f"{account.address} : {account.key.hex()} : {seed}")
        return Extractor.write_strings_to_file(string_array=private_keys)

    @staticmethod
    def read_from_txt(file_path: str = "seed_phrases.txt") -> list[str]:
        try:
            with open(file_path, "r") as file:
                return [line.strip() for line in file]
        except FileNotFoundError as e:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"Encountered an error while reading a TXT file '{file_path}': {e}.")

    @staticmethod
    def write_strings_to_file(string_array: list[str], file_path: str = "keys.txt") -> bool:
        try:
            with open(file_path, "w") as file:
                for string in string_array:
                    file.write(string + "\n")
                return True
        except FileNotFoundError as e:
            print(f"File '{file_path}' not found.")
            return False
        except Exception as e:
            print(f"Encountered an error while writing to a TXT file '{file_path}': {e}.")
            return False


def main() -> None:
    extractor = Extractor()
    extractor.extract()


if __name__ == "__main__":
    main()
