from distutils.command.sdist import sdist
from datasets import load_dataset
from datasets import DownloadConfig
#from datasets import total_allocated_bytes


def main():

    dataset = load_dataset("wikimedia/wit_base",cache_dir="D:/WIT")
    print("first row ", dataset[0])
    print("shape: ", dataset.shape)
    print(dataset.column_names)
    print(dataset.features)
    #print("The number of bytes allocated on the drive is", dataset.nbytes)
    
    sd=dataset['train'].select(range(100))
    dataset = load_dataset("wikimedia/wit_base",cache_dir="D:/WIT")  
    new_dataset = sd.map(lambda row: {'language': row['wit_features']['language'],'page_title': row['wit_features']['page_title'],'section_title': row['wit_features']['section_title'],'context_section_description': row['wit_features']['context_section_description'],'context_page_description': row['wit_features']['context_page_description'],'caption_reference_description': row['wit_features']['caption_reference_description']}, remove_columns=remli)
if __name__ == '__main__':
    main()
	