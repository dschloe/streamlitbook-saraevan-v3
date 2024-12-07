def sample_data():
    """Load a random dataset from seaborn's built-in datasets"""
    import seaborn as sns
    import random
    
    # Get list of available datasets
    dataset_names = sns.get_dataset_names()
    
    # Randomly select one
    selected_dataset = random.choice(dataset_names)
    
    # Load and return the selected dataset
    return sns.load_dataset(selected_dataset)


