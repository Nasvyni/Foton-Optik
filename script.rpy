# The script of the game goes in this file.

# Declare characters used by this game.
define Al = Character("Alawiyah")
define G = Character("Gilang")
define An = Character("Angel")
define Pr = Character("Pak Reksa")

#--------------chars!!!!!!!!!!!!!!!!!!!!!!!!!!11
image eileen happy = Transform("eileen_happy.png", zoom=0.527)
# ---------Alawiyah ----------------
image al normal = Transform("al.png", zoom=0.527)
image al down = Transform("al down.png", zoom=0.527)
image al liat = Transform("al liat.png", zoom=0.527)
image al worry = Transform("al worry.png", zoom=0.527)
image al browsraised = Transform("al browsraised.png", zoom=0.527)
image al mouthleft = Transform("al mouthleft.png", zoom=0.527)
image al shockraise = Transform("al shock raise mouthleft.png", zoom=0.527)
image al talk down = Transform("al talk down.png", zoom=0.527)

# -----------Angel -----
image an normal = Transform("an.png", zoom=0.527)
image an cry = Transform("an cry.png", zoom=0.527)
image an badmood = Transform("an badmood.png", zoom=0.527)
image an browsraised = Transform("an browsraised.png", zoom=0.527)
image an talk = Transform("an talk.png", zoom=0.527)
image an talkflirty = Transform("an talkflirty.png", zoom=0.527)
image an talk cry = Transform("an talk cry.png", zoom=0.527)
#
define audio.dis = "dis.mp3"
define audio.nor = "nor.mp3"


#k-------------bgs

image bg kls = "kls.png"
image bg kls old = "kls old.png"
image bg lorong = "lorong.png"
image bg kamar = "kmr.png"
image bg bakery = "bakery.png"
image bg jalan = "jalan.png"
image bg danau = "danau.png"
image bg semak = "semak.png"
image bg cg = "cg.png"



#-------------------------------------------------------------

label start:

    scene bg kls with dissolve

    show al normal at left
    play music nor

    Al "“Aku rela menjadi photon yang menghantam sebuah cermin dengan keras, diserap dengan elektron bebas dalam logam kaca, berosilasi elektron bebas kemudian memancarkan foton baru yang keluar dari cermin,”"
 
    show al liat at left
    Al "“jika itu berarti aku bisa memantulkan kecantikanmu yang mengguncangkan duniaku, bak–”"

    G "Ada seseorang yang menepukmu dari kiri. “Alawiyah, aya nu jatuh cinta, euy...!"
    
    G "Tong ngelantur wae, engké garalélo, siga Pak Reksa.” Gilang berbisik dari samping dengan aksen sunda tebalnya, aku bisa melihat senyuman jametnya" with vpunch

    show al worry at left
    "Oh.{p}{i}Oh.{/i} \n Dikira aku sedang membatin! Tak sengaja terucap."

    show al browsraised at left
    Al "“Kedengeran kaga ya?” Aku mengerutkan kening dan mendeham. “Sama… dia.” Aku melirik ke ujung kelas."

    G "Gilang hanya bisa memberiku ekspresi jijik. “Tah éta, ciri kahiji jadi monyét, monyét cinta—éh, budak ketang. Geus ah, mimiti ngaco, jung geura garap, ulanganna. Kerjakeun.”"

    hide al

    "Otakku terpaksa terlempar balik kedalam keputihan kertas ulangan PAI-ku, nomor 54, uraian pendek: {p} ‘Khalifah kedua dari Dinasti Abbasiyah adalah Khalifah Al-Mansur. Dari tahun berapa sampai tahun berapa al-Mansur menjadi Khalifah Dinasti Abbasiyah?’"

    "Lagi-lagi, pikiranku melayang. ‘...Ada batas keakuratan dalam mengetahui pasangan sifat fisik tertentu, seperti posisi dan momentum, secara bersamaan dalam sebuah partikel."
    
    "Dengan kata lain, semakin akurat suatu sifat diukur, semakin tidak akurat sifat lainnya dapat diketahui…’ Batinku,"

    "‘Singkatnya, bahkan partikel pun {i}tidak pasti!{/i}’" with hpunch

    show al down at left
    "Aku melirik ke ujung kelas. Ada Angel. Angel adalah salah satu teman terbaikku! Lebih dari hubungan fisika padaku. Walau dari jauh, terlihat bahwa dahi Angel dipenuhi keringat, poninya menempel. Bahkan dia pun gugup!"

    "…Atau ACnya butut."
    hide al

    scene bg kls old with dissolve
    
    "Lagian, kemarin, Gilang kecipratan air AC yang berwarna kuning pekat,{w} alhamdulillah we aku ga kena!{w} Tapi aku juga kasihan padanya, padahal,"

    "Ia baru saja memberiku nasehat cinta yang sangat baik, waktu-waktu dimana ia berbicara bahasa Indonesia berindikasi bahwa kata kata yang akan keluar sangat bijaksana dan lebih serius, dari biasanya:"

    G "“{b}{i}Kata-kata atau tindakan kebaikan akan terus bergema lama setelah momen itu berlalu, apa lagi di hati. Segalanya yang kau lakukan akan balik lagi”{/i}{/b}{p} atau sesuatu yang mirip dengan itu, aku lupa kata-kata pas Gilang."
    
    "Tapi, setelah mengevaluasi, aku bisa bilang itu benar sekali. Gelombang suara memantul dari dinding yang jauh dan {i}tetap berada di dalam ruangan{/i} lama setelah nada aslinya berhenti dimainkan, sampai keluar dari pendengaran biasa manusia."

    "Dan segalanya yang sebuah sistem lakukan, akan {b}{i}berbalik; bisa secara negatif atau positif{/i}{/b}"

    scene bg kls with dissolve

    Pr "Pak Reksa akhirnya berbicara, namun sekarang secara lambat, tak seperti biasanya. Matanya masih tekun pada handphone. {w}{cps=20}“2 Menit lagi…”{/cps}"

    "Mulutku terpaksa menggumamkan pertanyaan itu lagi, {i}Tuhan mungkin akan memberikan jawabannya langsung ke mulutku{/i}, siapa tahu?"

    show al browsraised at left
    Al "‘Khalifah kedua dari Dinasti Abbasiyah adalah Khalifah Al-Mansur. Dari tahun berapa sampai tahun berapa al-Mansur menjadi Khalifah Dinasti Abbasiyah?’"
    hide al

    "Tiba-tiba, ada suara gesekan sepatu dari depan kelas. Pak Reksa akhirnya sadar bahwa ia sedang mengawasi ulangan, dan menutup handphonenya."
    
    "“Ulangan {b}selesai.{/b}” Pak Reksa mengumumkan kepada kelas, tegas."

    "Sorak-surai langsung bergema keras di kelas, bahkan ada yang menaiki mejanya." with vpunch
    
    "Jam pun terlihat tak setuju, menunjukkan jam {b}11:21{/b}, masih ada {b}19 menit{/b} sebelum istirahat; dengan 19 menit itu, {i}aku bisa menyelesaikan ulangan PAI ini!{/i}"

    Pr "“Sekali lagi, saya yang bubarkan kelas. Bukan belnya, jangan komplen terus. Hey, syukur, udah disekolahin disini kok.”"

    "‘Gaadil! {w} Kalo pematerian doang, dia memperpanjang waktu kelas! Kalo ulangan, malah diperpendek!’ Batinku." with vpunch

    scene bg lorong with move

    "Di antara tempik sorak ramai kelas, tak terasa, kakiku sudah jalan sendiri ke pintu kelas. Aku bengong {i}lagi?{/i}"

    "Menengok kebelakang, kertas ulanganku sudah ada di meja guru, tertata rapih dengan kertas-kertas lainnya."
    
    "Pak Reksa juga sudah mulai menilai ulangan-ulangan siswa-siswi, dan, yang pertama dinilai adalah–dengan menyipitkan mata-aku bisa melihat nama yang tertulis diatasnya, {b}‘Angel.’{b}"

    "Sebenarnya ini hari yang aku tahu akan kurang beruntung untukkku,{w} karena PAI bukan hal favoritku."
    
    "Ya, kadang fisika memuat histori dari fisikawan, dan serunya membaca tentanag begimana fisikawan favoritku berinteraksi dengan fisikawan lain tak akan pernah habis."
    
    "Tapi, dalam urusan menghafal  tanggal, tempat dan alasan sebuah peristiwa...{p} aku kalah telak, dari {b}Angel.{/b}"

    "Sudah banyak guru yang secara terang terangan datang kepadaku dan Angel ketika sedang istirahat dan memuji Angel karena performanya yang baik di semua pelajaran-"
    
    "Semua, kecuali Pak Mardhiah. Pak Mardhiah berpesan bahwa seorang {i}All-Rounder{/i} seperti Angel bisa sangat baik di sekolah, tapi di luar sekolah, siswa-siswi harus memiliki sebuah keterampilan yang menonjol."

    "Sesakitnya kata-kata Pak Mardhiah untuk Angel-{i}yang sepertinya membutuhkan kesempurnaa untuk hidup{/i}-aku tetap menjunjung tinggi Angel, secara, intelektual. {w}Aneh, kadang kata-kata itu terasa asing di batinku sendiri."

    "Batinku yang sudah {i}berkali-kali sadar atas perasaanku sendiri.{/i}"

    "..."

    "Tiba tiba, ada suara."
    
    show an talk at right
    An "“Banf” Angel memberi emphasis pada ‘f’nya, panggilan biasa untukku. “Katanya mau ke BIP? Nonton?”"

    show al worry at left
    "Aduh! {p} Jujur saja, kata-kata Gilang benar benar menginspirasiku, dan aku sudah menyiapkan, kata-kata yang panjang dan berlika-liku untuk Angel." with hpunch


    show an talkflirty at right with dissolve
    "Tapi, {w}melihat kulit sedikit {i}tan{/i} dari lehernya yang tidak malu melihatkan kalung berwarna emasnya.{nw}"

    show an talk at right with dissolve
    "Tapi, melihat kulit sedikit {i}tan{/i} dari lehernya yang tidak malu melihatkan kalung berwarna emasnya.{fast} Jari anggunnya yang melambai padaku.{nw}"
    
    show an browsraised at right with dissolve
    "Tapi, melihat kulit sedikit {i}tan{/i} dari lehernya yang tidak malu melihatkan kalung berwarna emasnya. Jari anggunnya yang melambai padaku,{fast} gigi manisnya yang bertaring yang memabukkanku setiap ku pandang,"
    
    show an normal at right with dissolve
    "Bulu matanya yang panjang nan lentik,{nw}"

    show an talkflirty at right with dissolve
    "Bulu matanya yang panjang nan lentik,{fast} iris coklat gelap bola matanya yang bergelimang di cahaya matahari,{nw}"

    show an normal at right with dissolve
    "Bulu matanya yang panjang nan lentik, iris coklat gelap bola matanya yang bergelimang di cahaya matahari,{fast} semua pikir dan logisku buyar—"

    hide an

    show al mouthleft at left
    "Apa komposisi sebuah proton? Mungkin ada tipe quark yang bernama Angel? {i}Akan kucarikan. Atau boson gluon?{/i} Karena ia memikatku-"
    hide al
    
    "Pikiranku dipotong oleh dehaman Angel dan alisnya yang mengerut, menunggu respon dariku."
    
    show an badmood at right
    An "“Alawiyah?”"

    show al worry at left
    Al "Aku hanya bisa mengganguk. “Eh, panjang umur.”"

    show an talkflirty at right
    An "“...{p}Mikirin aku?”"

    show al liat at left
    Al "“Engga…?” Aku jawab, namun sedikit tak pasti"

    show an badmood at right
    "“Lah ngalpain bilang panjang umur dong?” Angel menghela napas."

    show al mouthleft at left
    "“…Gatau! Uda ah.” Aku mengangkat kedua lenganku keatas, menyerah."
    
    hide al
    show an normal at right
    "Angel terkikik melihat poseku, walau ketika tertawa, gerakannya tetap sangat anggun. {p} Dari belakang, terlihat Gilang yang sedang lewat, mengedipkan matanya padaku dan mengangkat botol ‘TEBS’-nya."

    "Dibelakang Gilang, siswa-siswi baru tumpah dari kelas-kelas lain—waktu istirahat sebenarnya baru mulai—dan tubuhku mulai tertabrak dengan tubuh siswa lain."
    
    show al normal at left
    "Aku memanggil Gilang, memikirkan tentang rencana sore ini. “Lang! Jadi nonton di BIP?”"
    hide al

    "“Teu! Barudak pada hayangna ka Joy n’ Fun BEC. sana sok, ka BIP.”"

    hide an
    stop music fadeout 1.0
    play music dis

    #day change now in al's room-----------------------------------------------------------------------------

    scene bg kamar with fade

    show al down at left
    "Dan, yap.{w} Karena itu, Angel meng-cancel dan aku menonton Shrek 19 {i}sendirian.{/i}"

    "{b}Sendiri.{/b}"

    show al worry at left
    "Mungkin Angel tidak suka one-on-one dengan {i}orang seperti aku?{/i}"
    hide al

    "{cps=10}…{/cps}"

    #-----------------------------------------------------------------------------

    stop music fadeout 1.0
    play music nor
    scene bg bakery with fade

    show al normal at left
    "Hari ini, aku pergi ke cabang Chez Enterprise yang aku tak pernah datangi; Chez Enterprise adalah toko pastry yang lumayan, mungkin Angel akan suka, dan {i}mengubah pikirannya tentang aku{/i}?"
    hide al

    $ current_room = "left" # this initializes the point'n'click segment to display the correct set of buttons.
    jump pnc_loop

label end:

    scene bg jalan

    show al down at left
    Al "Huff." with hpunch
    hide al

    show al worry at left
    "Kakiku seperti ingin copot. Capek sekali berjalan dari Chez Enterprise. Duh. Langsung KBM lagi... Kalau saja bisa bolos...."
    hide al

    "Tapi aku {i}harus{/i} memberi ini kepada Angel!"

    "Dalam kebodohan, aku berlari secepat cepatnya di trotoar. Tidak lama sebelum aku ngos-ngosan."

    show al mouthleft at left
    "Sebuah kalimat menusuk kepalaku yang nyut-nyutan; Aku pasti dimarahi Pak Reksa."

    "Nilai PAI!" with hpunch

    Al "Ah. Malas!"
    hide al

    "Akhirnya pandangku jatuh pada sebuah bangku di pinggir trotoar, dekat dengan sebuah toko tekstil."

    "Tak menunggu lama, aku langsung menduduki bangku."

    "Ayam mulai berkokok, itulah yang membangunkanku dari lamunanku, di pangkuanku tergeletak {b}pastri yang sudah dimakan 80\%-nya.{b}"

    "Pastri Angel!" with hpunch

    show al worry at left
    "‘Aduh! Kok aku bisa begini!’ Teriak batinku."
    hide al

    "Semoga Angel tak sadari keblunderan besarku, dengan doa itu, aku langsung berlari ke gerbang sekolah."

    scene bg lorong with move

    show an badmood at right
    "Angel menyilangkan tangannya, menatap tajam remah-remah kue red velvet yang sudah dimakan."

    if pnc_flags.get("Cromboloni") == True:
        "Angel menyilangkan tangannya, menatap remah-remah Cromboloni coklat yang sudah dimakan."
        show an talk cry at right
        An "Cromboloni padahal enak..."
    elif pnc_flags.get("Kue_Tomas") == True:
        "Angel menyilangkan tangannya, menatap tajam remah-remah kue Tomas The Engine yang sudah dimakan."
        show an badmood at right
        An "Kamu kira aku anak kecil?"
    elif pnc_flags.get("Cream_Tart") == True:
        "Aku mengambil Cream Tart bertuliskan '67'."
        show an browsraised at right
        An "67? Aga kekanak-kanakan."
    
    show an cry at right
    An "Angel menghembuskan napas. “Kok kamu bisa menghabiskan sebagian besar dan bilang ke aku 'cuman makan setengah'?”"

    show al mouthleft at left
    "Mulutku terbuka, tapi tak ada kata-kata yang keluar, padahal... 80\% termasuk setengah."
    hide al

    "Karena panik, otakku melayang {p} Waktunya fisika!"

    "Menurut Prinsip Heisenberg yang aku sering pikirkan, apa lagi di ulangan PAI, Anda tidak dapat secara bersamaan mengetahui posisi dan momentum suatu partikel—"
    
    "Sama seperti aku, tidak akan pernah dapat secara bersamaan mengetahui suasana hati gadis yang ku paling sayang dan kesalahan apa yang aku lakukan untuk memicunya."

    "(1) Tentukan posisi emosional kita pada sumbu x toleransi timbal balik...{p}(2) Terapkan kejutan kinetik kebodohan yang tiba-tiba untuk meningkatkan momentum...{p}(3)Amati fungsi gelombang yang benar-benar runtuh menjadi kekecewaan!"

    show an badmood at right
    An "Hm, ya.” Angel bergumam kecewa, lalu berbalik dan keluar dari kelas dengan marah."

    hide an

    "..." with hpunch

    stop music fadeout 1.0
    play music dis

    "——Oh.{p} Karena logikaku yang setengah matang, dia benar-benar {i}membenciku{/i}..."

    "Kupikir atom-atom kita terkunci, bersama, dengan gluon-gluon, berbagi keadaan spin di seluruh alam semesta."

    "Salah. Aku dan dia hanyalah dua partikel yang melayang menuju entropi dengan jalan masing-masing."

    "Waktunya fisika!" with hpunch

    "Untuk menghilangkan patah hati yang tak mencekam ini, aku akan menghitung energi dari gluon pemikat dan {i}memutuskan ikatan kita hingga nol...{/i}"

    "(1) Hitung total energi mekanis dari ingatan kita bersama...{p}∴ ME = ((1/2)mv² ) + (m × g × h)..."

    "(2) Perkenalkan penghalang yang berpotensial tinggi untuk memisahkan kita..."

    "(3) Paksa peluruhan partikel dan patahkan foto cetak kita menjadi dua...!" with vpunch

    "Tetapi tepat pada detik foto itu terbelah, Angel—yang tampaknya telah melupakan sesuatu dan mau balik lagi ke kelas untuk mengambilnya—membeku di mulut lorong."

    "Pandangannya turun pada dua potongan yang robek di tanganku, tiba-tiba berlinang air mata, sebelum dia berlari menyusuri koridor."

    "Meskipun aku kehilangan jejaknya, sebuah suara samar Gilang-Ia pasti sudah pulang, ini pasti rekaan imajinasiku-berbisik bahwa dia sedang menuju ke tempat kita dulu yang rimbun."

    "Jarak terpendek antara dua titik dalam ruang-waktu bukanlah garis lurus—melainkan bentuk berlekuk karena medan gravitasi!"

    "Dan saat ini, tarikan gravitasi dari penyesalanku melekukkan ruang-waktu itu sendiri, merasa bahwa ruang dimana aku berada terdistorsi."

    "Otakku balik ke kata-kata Gilang:"

    scene bg kls old with dissolve

    G "“{b}{i}Kata-kata atau tindakan kebaikan akan terus bergema lama setelah momen itu berlalu, apa lagi di hati. Segalanya yang kau lakukan akan balik lagi{/i}{/b}{p} atau sesuatu yang mirip dengan itu, aku lupa kata-kata pas Gilang."

    "Dan segalanya yang sebuah sistem lakukan, akan {b}{i}berbalik; bisa secara negatif atau positif{/i}{/b}"

    "Negatif. Hal yang aku lakukan negatif, dan hasilnya juga negatif.{p}(-)+(-)=(-)"

    scene bg lorong with dissolve

    "..."
    
    "Waktunya fisika!" with hpunch

    "Alasan aku menghabiskan malam mempelajari QFT bukanlah untuk OSN IPA. "

    "Itu agar aku bisa menghitung langkah yang tepat unruk menjembatani jarak di antara kita..."

    scene bg semak with move 

    "(1) Tuliskan garis lurus ke arah danau, tempat kita dulu.{p}(2) Memasukkan energi kinetikku berjalan dikurang hambatan udara...{p}(3) Percepat lurus menembus semak-semak halaman berduri, abaikan semua gesekan."
    
    "Ranting-ranting dan batu mencambuk wajahku, tetapi aku tidak merasakan sakit sama sekali"


    scene bg danau with move

    show al worry at left
    "Aku menerobos gerbang ke danau, dadaku terengah-engah, rambutku penuh dedaunan."
    hide al

    "Di sana dia! berdiri, menyeka air mata yang menetes di pipinya."

    "Aku terhuyung ke depan, jantungku berdetak sepuluh kali lipat biasanya, dan berseru:"

    stop music fadeout 1.0
    play music nor

    show al normal at left
    Al "“Angel! Aku-minta maaf!!”"

    show al mouthleft at left
    Al "“Aku mau jujur. Kamu...” Otakku melarang metafora fisika. “Dinasti Abbasiyah-ku!”"
    hide al

    show an cry at right
    An "“...Ngga lucu!”"

    show al browsraised at left
    Al "“Bukan candaan! Aku suka kamu, Ngel.”"
    hide al

    show an badmood at right
    "Muka Angel membeku. ‘Sia-sia.’Batinku, aku mulai berbalik badan."
    hide an

    "Bisa terdengar langkah kaki."
    scene bg cg

    "Ada berat sebuah kepala yang jatuh di belakang punggungku. Pandanganku pindah ke refleksi air danau, {p}Angel dibelakangku."

    "Ditengah air matanya, senyum kecil yang tulus muncul di wajahnya."

    "Satu-satunya jawabanku."

    Al "Selalu berbalik, toh."

    return