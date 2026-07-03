from src.data_loader import load_asset

def test_loader():

    df = load_asset("data/raw/TSLA.csv")

    assert len(df) > 0

    assert "Close" in df.columns