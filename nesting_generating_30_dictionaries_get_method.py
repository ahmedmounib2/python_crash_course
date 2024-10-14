aliens = []

for alien_number in range(30):
    alien= {'color':'green','speed':'slow','points':10}
    aliens.append(alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yelow'
        alien['speed']='medium'
        alien['points']=15
for alien in aliens[:5]:
    print(alien)