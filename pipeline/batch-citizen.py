d len(data['birthdate']) > 0


def convert_types(data):
    """Converts string values to their appropriate type."""
    from datetime import datetime
    data['name'] = str(data['name']) if 'name' in data else None
    data['id'] = int(data['id']) if 'id' in data else None
    data['hobby'] = str(data['hobby'])if 'hobby' in data else None
    data['favgame'] = str(data['favgame'])if 'favgame' in data else None
    data['birthdate'] = datetime.strptime(str(data['birthdate']),"%Y-%m-%d").strftime("%Y-%m-%d")  if 'birthdate' in data else None
    return data

def del_unwanted_cols(data):
    """Delete the unwanted columns"""
    del data['favgame']
    return data

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    known_args = parser.parse_known_args(argv)

    p = beam.Pipeline(options=PipelineOptions())

    (p | 'ReadData' >> beam.io.ReadFromText('gs://blankspace89783/batch/citizen.csv', skip_header_lines =1)
       | 'SplitData' >> beam.Map(lambda x: x.split(','))
       | 'FormatToDict' >> beam.Map(lambda x: {"name": x[0], "id": x[1], "hobby": x[2], "favgame": x[3], "birthdate": x[4]}) 
       | 'DeleteIncompleteData' >> beam.Filter(discard_incomplete)
       | 'ChangeDataType' >> beam.Map(convert_types)
       | 'DeleteUnwantedData' >> beam.Map(del_unwanted_cols)
       | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
           '{0}:citizen.c'.format(PROJECT_ID),
           schema=SCHEMA,
           write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))
    result = p.run()
    result.wait_until_finish()