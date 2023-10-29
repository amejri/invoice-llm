from time import time
from invoice_chatbot import InvoiceChatBot
import hydra
from omegaconf import DictConfig

@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):
    start = time()
    invoice_chat = InvoiceChatBot(**cfg)
    response = invoice_chat.chat_completion("please retrieve invoice date, and invoice number. im not interested in description, just give me these two values")
    print("response : ", response)
    end = time()
    
    print('#' * 100)
    print(f"Duration : {end - start} s")

if __name__ == "__main__":
    main()