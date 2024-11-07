import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image_01.jpg','Sundar Pichai'),
      ('image_02.jpg','Sundar Pichai'),
      ('image_03.jpg','Sundar Pichai'),
      ('image_04.jpg','Sundar Pichai'),
      ('image_05.jpg','Satya Nadella'),
      ('image_06.jpg','Satya Nadella'),
      ('image_07.jpg','Satya Nadella'),
      ('image_08.jpg','Satya Nadella'),
      ('image_09.jpg','Elon Musk'),
      ('image_10.jpg','Elon Musk'),
      ('image_11.jpg','Elon Musk'),
      ('image_12.jpg','Elon Musk'),
      ('image_13.jpg','Tim Cook'),
      ('image_14.jpg','Tim Cook'),
      ('image_15.jpg','Tim Cook'),
      ('image_16.jpg','Mark Zuckerberg'),
      ('image_17.jpg','Jeff Bezos'),
      ('image_18.jpg','Shantanu Narayen'),
      ('image_19.jpg','Shantanu Narayen')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('testmrunankbucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
