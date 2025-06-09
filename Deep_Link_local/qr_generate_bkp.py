from qr_code_generator import generate_deep_link, generate_qr_code
import json
import sys
import os

try:
    query_string = json.loads(sys.argv[1])
    deep_link = generate_deep_link(query_string)
    output_path = f"./qr_code_generator/output/{(query_string['context.bpp_id']).split('/')[0]}"
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    output_path = f"{output_path}/{query_string['message.intent.provider.id']}.png"

    # Example usage:
    generate_qr_code(deep_link, output_path)
except json.JSONDecodeError:
    print("Invalid JSON input.")
    raise
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    raise


# query_string = '{"context.bpp_id": "api.eksecond.in", "message.intent.provider.id": "6485f1878e3f6d5bd4df01b0", "context.domain": "RET10", "message.intent.provider.locations.0.id": "6485f1878e3f6d5bd4df01b0"}'
# python3 qr_generate.py '{"context.bpp_id": "biz.enstore.combiz.enstore.com", "message.intent.provider.id": "32b7d1ab-3ebe-485d-b824-c124737d8558", "context.domain": "ONDC:RET10"}'



#McDonald's = '{"context.bpp_id": "webapi.magicpin.in/oms_partner/ondc", "message.intent.provider.id": "11123577", "context.domain": "ONDC:RET11", "message.intent.provider.locations.0.id": "11123577"}'
#Bikkgane Biryani = '{"context.bpp_id": "webapi.magicpin.in/oms_partner/ondc", "message.intent.provider.id": "9938277", "context.domain": "ONDC:RET11", "message.intent.provider.locations.0.id": "9938277"}'
#Andhra Spices = python qr_generate.py '{"context.bpp_id": "webapi.magicpin.in/oms_partner/ondc", "message.intent.provider.id": "1984445", "context.domain": "ONDC:RET11", "message.intent.provider.locations.0.id": "1984445"}'
#Pizza Hut = python qr_generate.py '{"context.bpp_id": "webapi.magicpin.in/oms_partner/ondc", "message.intent.provider.id": "191498", "context.domain": "ONDC:RET11", "message.intent.provider.locations.0.id": "191498"}'
#Bagundi Andhra Kitchen = python qr_generate.py '{"context.bpp_id": "webapi.magicpin.in/oms_partner/ondc", "message.intent.provider.id": "9229486", "context.domain": "ONDC:RET11", "message.intent.provider.locations.0.id": "9229486"}'
#Biryani By Kilo = python qr_generate.py '{"context.bpp_id": "webapi.magicpin.in/oms_partner/ondc", "message.intent.provider.id": "2877782", "context.domain": "ONDC:RET11", "message.intent.provider.locations.0.id": "2877782"}'
#query_string = python qr_generate.py '{"context.bpp_id": "webapi.magicpin.in/oms_partner/ondc", "message.intent.provider.id": "10136794", "context.domain": "ONDC:RET11", "message.intent.provider.locations.0.id": "10136794"}'

#Kiko1 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "65bb6454d9b504f9bac9bdc5", "context.domain": "ONDC:RET10"}'
#Kiko2 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "65c0738dd9b504f9bacc594c", "context.domain": "ONDC:RET10"}'
#Kiko3 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "65cdea1dba7f49fa582bf61b", "context.domain": "ONDC:RET10"}'
#Kiko4 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "65d2f7429e5f55989673757b", "context.domain": "ONDC:RET10"}'
#Kiko5 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "64f1a41ff0131dba886a86e0", "context.domain": "ONDC:RET10"}'
#Kiko6 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "6530ff20088b80c8763046c2", "context.domain": "ONDC:RET10"}'

#Kiko3 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "65bb65aed9b504f9bac9beea", "context.domain": "ONDC:RET10"}'
#Kiko4 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "65cdea1dba7f49fa582bf61b", "context.domain": "ONDC:RET10"}'
#Kiko5 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "65d5b01a0789a104acc44055", "context.domain": "ONDC:RET10"}'
#Kiko6 = python qr_generate.py '{"context.bpp_id": "ondc.kiko.live/ondc-seller", "message.intent.provider.id": "64fad1410e017464d6ea2944", "context.domain": "ONDC:RET10"}'


#metro_use_case = python qr_generate.py '{"context.bpp_id": "metrobox.triffy.in", "message.intent.provider.id": "triffy-cmrl-rail-metro", "context.domain": "ONDC:TRV11"}'