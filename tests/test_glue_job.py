from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import Row

from glue_job import get_dynamic_frame_from_s3, write_dynamic_frame_to_s3


def test_get_dynamic_frame_from_s3(glue_context: GlueContext, setup_s3_data: dict[str, str]) -> None:
    source_s3_path = f"s3://{setup_s3_data['bucket_name']}/{setup_s3_data['key']}"
    result = get_dynamic_frame_from_s3(glue_context=glue_context, source_s3_path=source_s3_path)

    assert isinstance(result, DynamicFrame)
    assert result.count() == 3

    df = result.toDF()
    assert len(df.columns) == 3
    assert df.columns == ["col1", "col2", "col3"]

    rows = df.collect()
    assert rows == [
        Row(col1="val1", col2="1", col3="2000/01/01 01:00:00"),
        Row(col1="val2", col2="2", col3="2000/01/02 02:00:00"),
        Row(col1="val3", col2="3", col3="2000/01/03 03:00:00"),
    ]

def test_write_dynamic_frame_from_s3(
    glue_context: GlueContext,
    s3_bucket,
    sample_dynamicframe: DynamicFrame,
    get_s3_objects,
) -> None:
    file_key = "test_write_data"
    destination_s3_path = f"s3://{s3_bucket}/{file_key}"
    write_dynamic_frame_to_s3(
        glue_context=glue_context,
        dyf=sample_dynamicframe,
        destination_s3_path=destination_s3_path,
    )
    actual_s3_objects = get_s3_objects(s3_bucket=s3_bucket, prefix=file_key)

    assert len(actual_s3_objects) > 0
    assert any([object for object in actual_s3_objects if object.endswith(".parquet")])