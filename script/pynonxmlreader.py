import os,shutil
import string
a=[]
berkas='FileName'
jenis='Content'
family='Family'
genus='Genus'
spesies='Species'
hilang=['<FileName>','</FileName>','</Family>','<Family>','<Content>','</Content>','<Genus>','</Genus>','<Species>','</Species>','\t','\n',',']
"""Jumlah file xml"""
k=0

"""Jumlah file xml yang gagal dibaca"""
l=0
sukses=file('succeed','w')
gagal=file('failed','w')
for i in os.listdir('.'):
	if os.path.isdir(i):
		for j in os.listdir(i):
			if j.endswith('.xml'):
				k=k+1
				namafile=str(i)+'/'+str(j)
				with open(namafile) as f:
					dest1=''
					dest2=''
					dest3=''
					dest4=''
					dest=''
					src=''
					for baris in f:
						if berkas in baris:
							src=baris
							for b in hilang:
								if b in src:
									src=src.replace(b,"")
						if jenis in baris:
							dest1=baris
							for b in hilang:
								if b in dest1:
									dest1=dest1.replace(b,"")
								if dest1 == '':
									dest1='Undefined'
						if family in baris:
							dest2=baris
							for b in hilang:
								if b in dest2:
									dest2=dest2.replace(b,"")
								if dest2 == '':
									dest2='Undefined'
									
						if genus in baris:
							dest3=baris
							for b in hilang:
								if b in dest3:
									dest3=dest3.replace(b,"")
								if dest3 == '':
									dest3='Undefined'
						
						if spesies in baris:
							dest4=baris
							for b in hilang:
								if b in dest4:
									dest4=dest4.replace(b,"")
								if dest4 =='':
									dest4='Undefined'
									
					dest=dest1+'/'+dest2+'/'+dest3+'/'+dest4
					if not dest in a:
						a.append(dest)
						try:
							os.makedirs(dest)
							print('Directory '+dest+' created') 
						except:
							print('Directory '+dest+' not created')
					
					src=str(i)+'/'+src	
					print(dest,src)								
					try:
						shutil.copy(src,dest)
						print('File '+src+' copied')
						sukses.write(namafile+'\n')
					except:
						print('File '+src+' not copied')
						l=l+1
						gagal.write(namafile+'\n')
					
					f.close()
print(str(l)+' dari '+str(k)+' citra gagal disalin')
gagal.close()
sukses.close()
for i in a:
	print i
