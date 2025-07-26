import json
import urllib.request


def download_soo_list(key, sdate, edate):
    """
    Downloads the SOO list for a given year and month.
    
    Args:
        key (str): The API key for authentication.
        year (int): The year for which to download the SOO list.
        month (int): The month for which to download the SOO list.
    
    Returns:
        dict: The SOO list data.
    """
    url = f"https://www.nifs.go.kr/OpenAPI_json?id=sooList&key={key}&sdate={sdate}&edate={edate}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode("euc-kr"))
    return data["body"]["item"]


def download_soo_code(key, gru_nam):
    """
    Downloads the SOO code for a given SOO name.
    
    Args:
        key (str): The API key for authentication.
        gru_nam (str): The name of the SOO.
    
    Returns:
        dict: The SOO code data.
    """
    url = f"https://www.nifs.go.kr/OpenAPI_json?id=sooCode&key={key}&gru_nam={gru_nam}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode("euc-kr"))
    return data["body"]["item"]

if __name__ == "__main__":
    key = "qPwOeIrU-2506-KUVBOC-1211"
    for year in range(1961, 2025):
        try:
            sdate = f"{year}0101"
            edate = f"{year}1231"
            soo_list = download_soo_list(key, sdate, edate)
            with open(f"soo_list_{year}.json", "w", encoding="utf-8") as f:
                json.dump(soo_list, f, ensure_ascii=False, indent=4)
            print(f"Downloaded SOO list for year: {year}")
        except Exception as e:
            print(f"Failed to download SOO list for {year}: {e}")
    
    for gru_nam in ["E", "W", "S", "EC"]:
        try:
            soo_code = download_soo_code(key, gru_nam)
            with open(f"soo_code_{gru_nam}.json", "w", encoding="utf-8") as f:
                json.dump(soo_code, f, ensure_ascii=False, indent=4)
            print(f"Downloaded SOO code for {gru_nam}")
        except Exception as e:
            print(f"Failed to download SOO code for {gru_nam}: {e}")

    print("Download completed.")