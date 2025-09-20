import instaloader

def download_reel(url:str):
    loader = instaloader.Instaloader()

    try:
        shortcode = url.split("/")[-2]

        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target="downloaded_reels")
        print(f"\n Reel downloaded! saved in 'downloaded_reels/{shortcode}'\n")
              
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("=== Instagram Reel Downloader ===")
    reel_url = input("ENTER THE URL :")
    download_reel(reel_url)
    input("Press Enter to EXIT...")