encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()


encrypted_message = """Tgeoq ooe bb oo  vohwtynis,o" niissaemwsth  unrhn  oa aaswion eamntioaoaopiesni  dhvtrt eeiip cm EfDcEn eutyan  w"rtnssa as uedwres ieacee nipcd ehi irnbseg isnmtcr douefc mcllxr  tttdmesewp onno rocdls bqnaieacurcehaii nowttl raos ttou eayet enriccimel te ia aAo. eapkoo  rnmehsua dinm leosptevt eenesddntimstbeteenn dits eeesa.aIl uoxrtRoA Mo.tdafml ,hp oaitesa  exgllndthoe  scte ch ttydutteirkcthii  euns  tAd es  oa laGemtT ye ttoul nh."""

message = list(encrypted_message)

start, end = 1, len(message) - 2

while start < end:
    message[start], message[end] = message[end], message[start]
    start += 2
    end -= 2
decrypted_message = ''.join(message)
print(decrypted_message)
