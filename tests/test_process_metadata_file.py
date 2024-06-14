from pathlib import Path
from typing import Final
import pandas as pd
import os
import pytest
from rcx_tk.process_metadata_file import read_file, save_dataframe_as_tsv, process_metadata_file

__location__: Final[Path] = Path(__file__).parent.resolve()

@pytest.fixture 
def dataframe():
    d = {
        'File path': [
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\1_instrumental blank_01.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\4_Alkane mix_04.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\6_instrumental blank_06.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\7_procedural blank_07.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\8_QC non-dilute_08.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\11_QC 16_11.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\12_QC 8_12.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\15_QC non-dilute_15.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\18_QC 4 _18.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\19_QC 8_19.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\29_instrument blank_29.raw"
        ],
        'File name': [
            "1_instrumental blank_01",
            "4_Alkane mix_04",
            "6_instrumental blank_06",
            "7_procedural blank_07",
            "8_QC non-dilute_08",
            "11_QC 16_11",
            "12_QC 8_12",
            "15_QC non-dilute_15",
            "18_QC 4 _18",
            "19_QC 8_19",
            "29_instrument blank_29"
        ],
       'Type': [
            "Standard",
            "Standard",
            "Standard",
            "Blank",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "Standard"
       ],
       "Class ID": [
            3,
            5,
            3,
            6,
            2,
            2,
            2,
            2,
            2,
            2,
            3
       ],
       "Batch": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
       ],
      "Analytical order": [
            1,
            4,
            6,
            7,
            8,
            11,
            12,
            15,
            18,
            19,
            29
      ],
      "Inject. volume (uL)": [
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6
      ],
       "Included": [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True
       ]
    }

    return pd.DataFrame(data = d)

@pytest.fixture 
def dataframe2():
    d = {
        'File name': [
            "1_instrumental blank_01",
            "4_Alkane mix_04",
            "6_instrumental blank_06",
            "7_procedural blank_07",
            "8_QC non-dilute_08",
            "11_QC 16_11",
            "12_QC 8_12",
            "15_QC non-dilute_15",
            "18_QC 4 _18",
            "19_QC 8_19",
            "29_instrument blank_29"
        ],
       'Type': [
            "Standard",
            "Standard",
            "Standard",
            "Blank",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "Standard"
       ],
       "Class ID": [
            3,
            5,
            3,
            6,
            2,
            2,
            2,
            2,
            2,
            2,
            3
       ],
       "Batch": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
       ],
      "Analytical order": [
            1,
            4,
            6,
            7,
            8,
            11,
            12,
            15,
            18,
            19,
            29
      ],
      "Inject. volume (uL)": [
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6
      ],
       "Included": [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True
       ]
    }
    
    return pd.DataFrame(data = d)
 
@pytest.fixture 
def processed_dataframe():
    d = {
        'sampleName': [
            "1_instrumental_blank_01",
            "4_Alkane_mix_04",
            "6_instrumental_blank_06",
            "7_procedural_blank_07",
            "8_QC_non-dilute_08",
            "11_QC_16_11",
            "12_QC_8_12",
            "15_QC_non-dilute_15",
            "18_QC_4_18",
            "19_QC_8_19",
            "29_instrument_blank_29"
        ],
       'sampleType': [
            "Standard",
            "Standard",
            "Standard",
            "Blank",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "Standard"
       ],
       "class": [
            3,
            5,
            3,
            6,
            2,
            2,
            2,
            2,
            2,
            2,
            3
       ],
       "batch": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
       ],
      "injectionOrder": [
            1,
            4,
            6,
            7,
            8,
            11,
            12,
            15,
            18,
            19,
            29
      ]
    }

    return pd.DataFrame(data = d)


@pytest.mark.parametrize("file_name",
                         ["batch_specification1.csv", "batch_specification1.xlsx", "batch_specification1.txt"])
def test_read_file(file_name, dataframe):
    file_path = __location__.joinpath("test_data", file_name)
    #file_path = os.path.join("tests", "test_data", file_name)
    actual = read_file(str(file_path))
    assert actual.equals(dataframe)

def test_read_file_error(dataframe):
    file_path = os.path.join("tests", "test_data", "batch_specification1.prn")
    with pytest.raises(ValueError, match = r"Unsupported file format. Please provide a CSV, Excel, or TSV file."):
        read_file(file_path)

def test_save_dataframe_as_tsv(dataframe, tmp_path):
    # Does the written tsv have the same structure as the original dataframe?
    # Is there any tsv in the directory?
    out_path = os.path.join(tmp_path, "batch_specification1.tsv")
    save_dataframe_as_tsv(dataframe, out_path)
    actual = pd.read_csv(out_path, sep='\t')
    assert actual.equals(dataframe)

def test_read_save_dataframe_as_tsv_error(dataframe, tmp_path):
    out_path = os.path.join(tmp_path, "batch_specification1.prn")
    with pytest.raises(ValueError, match = r"Unsupported file format. Please point to a TSV file."):
        save_dataframe_as_tsv(dataframe, out_path)

def test_process_metadata_file(processed_dataframe, tmp_path):
    # expected  = processed_dataframe
    file_path = os.path.join("tests", "test_data", "batch_specification1.csv")
    out_path = os.path.join(tmp_path, "processed_batch_specification1.tsv")
    process_metadata_file(file_path, out_path) 
    actual = pd.read_csv(out_path, sep='\t')
    assert actual.equals(processed_dataframe)