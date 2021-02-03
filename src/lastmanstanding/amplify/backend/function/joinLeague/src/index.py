import json
import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key

def handler(event, context):
  print('received event:')
  print(event)
  result = json.loads(event['body'])
  leagueCode = result["leagueCode"]
  sub = result["sub"]
  fname = result['firstName']
  lname = result['lastName']
  fullName = fname + ' ' + lname
  username = result["username"]

  client = boto3.client('dynamodb')

  data = client.query(
    TableName = "LeaguesDB-develop",
    IndexName = "invitationCode-LeagueID-index",
    ExpressionAttributeValues={
        ':v1': {
            'S': leagueCode
        },
    },
    KeyConditionExpression='invitationCode= :v1'
  )

  resp = data['Items']
  leagueID = resp[0]['LeagueID']['S']

  leaguePlayerID = leagueID +'/'+ sub
  admin = "No"
  createdDate = str(datetime.today())
  dynamodb = boto3.resource('dynamodb')

  tableName = "LeaguePlayerDB-develop"
  table = dynamodb.Table(tableName)

  table.put_item(
      Item={
				'LeaguePlayerID': leaguePlayerID,
				'LeagueID': leagueID,
				'CurrentPick': " ",
				'PickedTeams': [],
				'Admin': admin,
        'fullName': fullName,
				'Username': username,
				'playerStatus': "In",
				'createdTime': createdDate,
				'UnpickedTeams': ["Manchester United FC","Manchester City FC","Leicester City FC","Liverpool FC","Tottenham Hotspur FC","Everton FC","Chelsea FC","Southampton FC","West Ham United FC","Sheffield United FC","Arsenal FC","Aston Villa FC","Leeds United FC","Crystal Palace FC","Wolverhampton Wanderers FC","Newcastle United FC","Brighton & Hove Albion FC","Burnley FC","Fulham FC","West Bromwich Albion FC"]
      })

  table3 = dynamodb.Table('PlayerDB-develop')
  data = table3.query(
    KeyConditionExpression=Key('Sub').eq(sub)
  )

  resp = data['Items']
  leagueIDs = resp[0]['leagueIDs']
  leagueIDs.append(leagueID)
  table3.update_item(
    Key={
            'Sub': sub
        },
        UpdateExpression="set leagueIDs=:l",
        ExpressionAttributeValues={
            ':l': leagueIDs
        },
        ReturnValues="UPDATED_NEW"
  )

  return {
    'statusCode': 200,
    'headers': {
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
    'body': "hello"
    }

