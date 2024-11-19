#!/usr/bin/env python3

from flask import Flask

# To turn debugging on:
# FLASK_DEBUG=1 ./server.py

# Setup the webapp:
app = Flask(__name__)


def timeline():
    return """
    <div>
    <p>
      <br/><br/><br/><br/><br/>
    </p>
    <hr/>
    </div>

    <font size="-1">
    <div>
    <h2>Lucy Mensing Timeline</h2>
    <table>
    <tr>
    <!-- EVENTS -->
    <td></td>
    <td width="30px"></td>
    <td><a href="/expressionism"><i>Early interest in expressionist painting</i></a></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><a href="/recollections"><i>Reminiscences from 1989</i></a></td>
    </tr>
    <tr>
    <!-- VERTICAL BARS TO EVENTS -->
    <td></td>
    <td></td>
    <td><div class="vl"></div></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><div class="vl"></div></td>
    </tr>
    <tr>
    <!-- TIME PERIODS -->
    <td width="100px">
    <a href="/"><i>Start</i></a>&nbsp;&nbsp; &#8594;
    </td>
    <td>

    </td>
    <td width="160px">
    <a href="/early_life_edu">Early life and education</a>
    </td>
    <td width="150px">
    <a href="/goettingen">Time in G&ouml;ttingen</a>
    </td>
    <td width="150px">
    <a href="/tuebingen">Time in T&uuml;bingen</a>
    </td>
    <td width="150px">
    <a href="/muenchen_koenigsberg">Time in M&uuml;nchen, K&ouml;nigsberg and Jena</a>
    </td>
    <td width="175px">
    <a href="/soviet">Time in the Soviet Union</a>
    </td>
    <td width="150px">
    <a href="/jena_return">Return to Jena</a>
    </td>
    </tr>
    <tr>
    <!-- VERTICAL BARS TO EVENTS -->
    </tr>
    <td></td>
    <td></td>
    <td></td>
    <td><div class="vl"></div></td>
    <td></td>
    <td></td>
    <td></td>
    <td><div class="vl"></div></td>
    <tr>
    <!-- EVENTS -->
    <td></td>
    <td></td>
    <td></td>
    <td><a href="/important_papers"><i>Three important papers</i></a></td>
    <td></td>
    <td></td>
    <td></td>
    <td><a href="/belated_recognition"><i>Belated recognition</i></a></td>
    </tr>
    </table>
    <br/>
    <hr/>
    <br/>
    <p><a href="/acknow">Acknowledgements</a>&nbsp;&nbsp;&nbsp;<a href="/biblio">Bibliography</a>&nbsp;&nbsp;&nbsp;<a href="/gallery">Picture gallery</a></p>
    </div>
    </font>
    """


# TODO: Incorporate the WiHQP logo (See Margriet's email of 2024-10-28).
def generate_header(title, background_image):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Lucy Mensing Web Exhibit Mock-Up -- {title}</title>
    <style>
      td, th {{
        vertical-align:top;
      }}
      div {{
        width:750px;
        margin:auto;
      }}
      body {{
        background-color: #36454f;
        color: yellow;
        a {{
          color: gold;
        }}
        background-image: url('{background_image}');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
      }}
      .vl {{
        border-left: 2px solid yellow;
        height: 20px;
        width: 5px;
      }}
      .hangin {{
        padding-left: 22px ;
        text-indent: -22px ;
      }}
      figure {{
        display: inline-block;
        text-align: center
      }}
      img {{
        border: 1px solid white;
      }}
    </style>
    </head>
    """


@app.route("/omitted")
def omitted():
    title = "Page omitted"
    header = generate_header(title, "/static/mensing_index.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>
    """
    return html


@app.route("/pioneer_talk")
def pioneer_talk():
    title = "Lucy Mensing: Forgotten Quantum Pioneer (presentation by Michel Janssen)"
    header = generate_header(title, "/static/mensing_index.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>
    <p>
    <strong>Abstract: </strong>Lucy Mensing obtained her PhD in theoretical
    physics working with Pauli in Hamburg in early 1925, then spent a year in
    G&ouml;ttingen right around the time matrix mechanics was developed there. After
    that, she went to T&uuml;bingen, where many of the spectroscopic data were
    obtained that drove the transition from the old to the new quantum
    theory. It is hard to imagine better places to be in those years for young
    quantum theorists trying to make a name for themselves. Mensing made some
    important contributions to the early development of quantum mechanics. In
    this talk, I will examine these promising early stages of Mensing’s career
    and ask why she gave it up only three years in. I argue that it was not
    getting married and having children that forced Lucy Mensing, now Lucy
    Sch&uuml;tz, out of physics but that it was the other way around: frustration
    about her own research and a distaste for the cutthroat competitive
    mentality she encountered made her choose family over physics.
    </p>

    <p>
    Based on joint work with Gernot Münster (University of Münster) in the context
    of the WiHQP project (Women in the History of Quantum Physics)
    </p>

    <p>
    Video on <a href="https://www.youtube.com/watch?v=5eogMITfwCg">YouTube</a>
    </p>

    <p>
    Slides on <a href="/omitted">Google Drive</a>
    </p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/")
def index():
    # FYI To save the images from Michel's page, copy-paste into a libreoffice writer doc
    # and then save the image to a file from there (stupid Google).
    title = "Lucy Mensing (1901&ndash;1995)"
    header = generate_header(title, "/static/mensing_index.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>
    <p>
    Lucy Mensing obtained her PhD in theoretical physics in Hamburg in early
    1925. She then spent a year in G&ouml;ttingen right around the time matrix
    mechanics was developed there to which she made some important
    contributions herself. She clarified the new rules for quantizing angular
    momentum and applied them to diatomic molecules. She then went to T&uuml;bingen,
    where she struggled to explain the Ramsauer effect. While in T&uuml;bingen, she
    married fellow physicist Wilhelm Sch&uuml;tz (1900–1972). Lucy Mensing, now Lucy
    Sch&uuml;tz, followed her husband to Munich and from there to K&ouml;nigsberg (now
    Kaliningrad) and Jena. The couple would have four children. Starting a
    family meant the end of her career as an independent researcher in
    physics.
    </p>
    <p>
    Use the timeline below to navigate the exhibit or start <a href="/early_life_edu">here</a>.
    </p>

    <h3>Further resources</h3>
    <ul>
    <li><a href="/gallery">Picture gallery</a></li>
    <li><a href="/pioneer_talk">Presentation by Michel Janssen: Lucy Mensing: Forgotten Quantum Pioneer</a></li>
    </ul>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/gallery")
def gallery():
    title = "Picture gallery"
    header = generate_header(title, "")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <figure>
    <img width="480" src="static/mensing_early.jpg"><br/>
    <figcaption>Lucy Mensing in 1926</figcaption>
    </figure>

    <figure>
    <img width="480" src="static/mensing_after.jpg"><br/>
    <figcaption>Lucy Mensing in 1927</figcaption>
    </figure>

    <figure>
    <img width="480" src="static/mensing_index.jpg"><br/>
    <figcaption>Lucy Mensing in 1928</figcaption>
    </figure>

    <figure>
    <img width="480" src="static/mensing_index.jpg"><br/>
    <figcaption>Lucy Mensing in 1928</figcaption>
    </figure>

    <figure>
    <img width="640" src="static/excursion1.jpg"><br/>
    <figcaption>Excursion of Tübingen physicists to the Black Forest, May
      1927. Lucy Mensing and Wilhelm Schütz (with backpacks and their hands in
      their pockets on opposite sides of an unidentified individual). Second
      from left: Alfred Landé (with glasses).</figcaption>
    </figure>

    <figure>
    <img width="640" src="static/excursion2.jpg"><br/>
    <figcaption>Excursion of Tübingen physicists to the Black Forest, May
      1927. Lucy Mensing reclining in the grass in the foreground. Note the
      sign on the shed behind her that says “Freudenstadt” and “Igelsberg” (now
      part of Freudenstadt).</figcaption>
    </figure>

    <figure>
    <img width="480" src="static/engaged.jpg"><br/>
    <figcaption>Lucy Mensing and Wilhelm Schütz engaged, 1927</figcaption>
    </figure>

    <figure>
    <img width="480" src="static/family.jpg"><br/>
    <figcaption>Wilhelm and Lucy Schütz with their first son Jürgen (born
      1930), Niendorf/Timmendorfer Strand, Schleswig-Holstein,
      1933</figcaption>
    </figure>

    <figure>
    <img width="640" src="static/with_heisenberg.jpg"><br/>
    <figcaption>Lucy Schütz (center) in conversation with Werner Heisenberg and
      an unidentified woman at a Joint meeting of the Physical Societies of
      East and West Germany in Berlin, 1952.</figcaption>
    </figure>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/biblio")
def biblio():
    title = "Bibliography"
    header = generate_header(title, "/static/mensing_index.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p class="hangin">Max Born, Werner Heisenberg and Pascual Jordan. “Zur Quantenmechanik
      II.” <em>Zeitschrift für Physik</em> 35 (1926) 557–615. English
      translation: pp. 321–385 in Bartel Leendert van der Waerden (Ed).
      <em>Sources of Quantum Mechanics</em>. New York: Dover, 1968.</p>
    <p class="hangin">Hilding Faxén and Johan Peter Holtsmark, “Beitrag zur Theorie des
      Durchganges langsamer Elektronen durch Gase.” <em>Zeitschrift für Physik
      </em>45 (1927): 307–324. DOI: <a href="https://doi.org/10.1007/BF01343053"><em>https://doi.org/10.1007/BF01343053</em></a>.</p>
    <p class="hangin">Lucy Mensing, <em>Beitrag zur Theorie der Verbreiterung von
        Spektrallinien</em>. Ph.D. thesis, Hamburg University, 1925.</p>
    <p class="hangin">Lucy Mensing, “Zur Störungsmechanik der Molekülmodelle.”
      <em>Zeitschrift für Physik</em> 34 (1925): 602–610. DOI:
      https://doi.org/10.1007/BF01328505.</p>
    <p class="hangin">Lucy Mensing, “Beitrag zur Theorie der Verbreiterung von
      Spektrallinien.” <em>Zeitschrift für Physik</em> 34 (1925): 611–621.
      DOI: https://doi.org/10.1007/BF01328506. </p>
    <p class="hangin">Lucy Mensing, “Die Rotations-Schwingungsbanden nach der
      Quantenmechanik.” Zeitschrift für Physik, 36 (1926) 814–823. DOI: <a href="https://doi.org/10.1007/BF01400216"><em>https://doi.org/10.1007/BF01400216</em></a>.</p>
    <p class="hangin">Lucy Mensing,  “Die Intensitäten der Zeemankomponenten beim
      partiellen Paschen-Back-Effekt.” <em>Zeitschrift für Physik</em> 39
      (1926): 24–28. DOI: https://doi.org/10.1007/BF01321897.</p>
    <p class="hangin">Lucy Mensing, “Zur Theorie des Zusammenstoßes von Atomen mit
      langsamen Elektronen.” <em>Zeitschrift für Physik</em> 45 (1927):
      603–609. DOI: https://doi.org/10.1007/BF01331923.</p>
    <p class="hangin">Lucy Mensing and Wolfgang Pauli, “Über die Dielektrizitätskonstante
      von Dipolgasen nach der Quantenmechanik.” <em>Physikalische
        Zeitschrift</em> 27 (1926): 509–512.</p>
    <p class="hangin">Charles Midwinter and Michel Janssen,  “<a href="https://www.mprl-series.mpg.de/studies/2/8/index.html"><em>Kuhn
          Losses Regained</em></a>: Van Vleck from Spectra to Susceptibilities.
      Pp. 137–205 in: Massimiliano Badino and Jaume Navarro (Eds.),
      <em>Research and Pedagogy: A History of Early Quantum Physics through
        its Textbooks</em>. Berlin: Edition Open Access, 2013.</p>
    <p class="hangin">Gernot Münster, “<a
                          href="https://pro-physik.de/zeitschriften/download/19857"><em>(K)eine
          klassische Karriere?</em></a>” <em>Physik Journal</em> 19 (6) (2020):
      30–34</p>
    <p class="hangin">Gernot Münster and Michel Janssen, “<a href="/omitted"><em>Angular
          and Career Momentum: What Lucy Mensing Contributed to Physics and Why
          She Left the Field</em></a>.” Ch. 4 in: Patrick Charbonneau, Michelle
      Frank, Margriet van der Heijden, Daniela Monaldi (Eds.), <em>Women in
        the History of Quantum Physics. Beyond Knabenphysik</em>. Cambridge:
      Cambridge University Press, expected 2025.</p>
    <p class="hangin">John H. Van Vleck, “Magnetic Susceptibilities and Dielectric
      Constants in the New Quantum Mechanics.” <em>Nature</em> 118 (1926):
      226–227. DOI: https://doi.org/10.1038/118226c0.</p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/acknow")
def acknow():
    title = "Acknowledgements"
    header = generate_header(title, "/static/mensing_index.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>
    The WiHQP website team would like to thank Dr. Dorothea Roloff, Lucy
    Sch&uuml;tz-Mensing’s youngest daughter, for allowing us to post manuscripts and
    photographs of her mother and, more generally, for providing much of the
    biographical information used for this website.
    </p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/expressionism")
def expressionist():
    title = "Mensing's Early Appreciation for Expressionist Painting"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>Much has been made of the parallels between modern physics and
    modern art, especially between Einstein and Picasso. There is little
    evidence, however, that the pioneers of
    modern physics had any appreciation for the pioneers of modern art. Lucy
    Mensing, however, took an early interest in German expressionist
    painting. Writing about a visit to the Ludwig Museum in Cologne in a letter
    of August 1982 to <a
    href="https://en.wikipedia.org/wiki/Ernst_Ising"><em>Ernst Ising</em></a>,
    a friend from her student days in Hamburg, and his wife Hanna, she recalls
    seeing one of <a href="https://en.wikipedia.org/wiki/Franz_Marc"><em>Franz
    Marc</em></a>’s paintings in the Hamburger Kunsthalle as a student:</p>
    
    <p>&lsquo;The painting “Wild Boars” of Marc reminded me of the Hamburg
    “Mandrill”. It used to be taunted and mocked in my youth. Then the
    professor for literature, in a class we, i.e., Ernst and I, attended once a
    week, discussed the Mandrill—the colorful animal in the lush jungle—and we
    saw it with different eyes. I assume that one was also by Franz Marc. The
    painting is said to have disappeared during the war. Whether the Nazis had
    already taken it earlier and sold it to US?&rsquo;</p>

    <p><i>German original:</i></p>

    <p><i>Bei einem Bild ‘Wildschweine’ von Marc fiel mir der Hamburger ‘Mandrill’
    ein. Der wurde in meiner Jugend beschimpft und l&auml;cherlich gemacht. Dann hat
    der Lit.-Professor bei dem wir, d.h. Ernst und ich, einmal in der Woche ein
    Kolleg h&ouml;rten, den Mandrill besprochen – das farbenpr&auml;chtige Tier in dem
    &uuml;ppigen Urwald – da sah man es mit anderen Augen an. Ich nehme jetzt an,
    daß der auch von Franz Marc war. Das Bild soll im Krieg verschwunden
    sein. Ob die Nazis es schon fr&uuml;her beseitigt und nach Amerika verkauft
    hatten?</i></p>

    <p>
    <table>
    <tr>
    <td>
    <figure>
    <img width="240" src="static/mandrill.jpg"><br/>
    <figcaption>Franz Marc, “The Mandrill” (1913). Pinakothek der Moderne, Munich.</figcaption>
    </figure>
    </td>
    <td witdh="10px"></td>
    <td>
    <figure>
    <img width="240" src="static/wild_boars.png"><br/>
    <figcaption>Franz Marc, “Wild Boars” (1913). Ludwig Museum, Cologne.</figcaption>
    </figure>
    </td>
    </tr>
    </table>
    </p>

    <p>As Mensing surmised, “The Mandrill” was indeed among dozens of <a
    href="https://www.welt.de/print/wams/hamburg/article121973736/Im-Namen-des-Fuehrers.html"><em>paintings
    the Nazis confiscated from the Hamburger Kunsthalle</em></a> in 1937.</p>

    <p>Earlier that same year (1982), Lucy Sch&uuml;tz and the Isings had admired
    paintings by <a href="https://en.wikipedia.org/wiki/Emil_Nolde"><em>Emil
    Nolde</em></a> and others in the Kunsthalle in Kiel (where Lucy’s sister
    Hildegard lived).</p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/important_papers")
def important_papers():
    title = "Mensing's Three Most Important Papers"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <h1>{title}</h1>
    <br/><br/><br/><br/>
    <div>

    <ol>
    <li>“<em>Die Rotations-Schwingungsbanden nach der Quantenmechanik</em></a>.”
    <em>Zeitschrift f&uuml;r Physik</em> 36 (1926): 814–823 <a
    href="https://doi.org/10.1007/BF01400216"><em>DOI</em></a></li>
    <li>With Wolfgang Pauli, “<em>&UUML;ber die Dielektrizit&auml;tskonstante von
    Dipolgasen nach der Quantenmechanik</em>.” <em>Physikalische
    Zeitschrift</em> 27 (1926), 509–512.</li>
    <li>“<em>Die Intensit&auml;ten der Zeemankomponenten beim partiellen
    Paschen-Back-Effekt</em>.” <em>Zeitschrift f&uuml;r Physik</em> 39
    (1926): 24–28. <a
    href="https://doi.org/10.1007/BF01321897"><em>DOI</em></a></li>
    </ol>

    <br/>
    <hr/>
    <br/>

    <p>Mensing arrived in G&ouml;ttingen while matrix mechanics was taking shape and
    she took full advantage of having a front row seat for these
    developments. She wrote two important papers on the new quantum mechanics
    during the year following her PhD and co-authored another one. She wrote
    the first one in G&ouml;ttingen but the second and the third at least partly
    after she had gone back home to Hamburg (where her co-author Pauli was
    still based in 1926 although he also visited G&ouml;ttingen and Copenhagen). She
    was the first to apply the new quantum mechanics to diatomic molecules,
    which she had already written a paper about in the context of the old
    quantum theory in 1923/24 in Hamburg (which was only published, however,
    right before the one on the new quantum quantum mechanics)</p>

    <p>In the first paper, entitled “The rotation-vibration bands according to
    quantum mechanics,” Mensing applied the new rules for the quantization of
    angular momentum—first published in early 1926 in the famous
    <em>Dreim&auml;nnerarbeit</em> (Three-Man-Paper) of Born, Heisenberg and Jordan
    (<a href="https://doi.org/10.1007/BF01379806"><em>DOI</em></a>)—to diatomic
    molecules and solved a puzzle that the spectrum of such molecules had posed
    for the old quantum theory. In the process she sharpened the quantization
    rule: Born, Heisenberg and Jordan had shown that the quantum number for
    angular momentum could take on integer <em>or half-integer</em>
    values. Mensing showed that <em>orbital</em> angular momentum (as opposed
    to intrinsic angular momentum or spin) could only take on integer
    values.</p>

    <p>Impressed by these results, Pauli invited her to collaborate     with
    him on a related puzzle concerning the electric susceptibility in diatomic
    gases. Their solution of this puzzle, in a paper entitled “On the
    dielectric constant of dipole gases according quantum mechanics,” was one
    of the first successes of the new quantum mechanics outside of the field of
    spectroscopy for which the theory was originally developed. This was
    emphasized by <a
    href="https://en.wikipedia.org/wiki/John_Hasbrouck_Van_Vleck"><em>John Van
    Vleck</em></a> who found the same result as Mensing and Pauli, using some
    results on angular momentum from Mensing’s earlier paper on
    rotation-vibration bands. In an interview for the <a
    href="https://search.amphilsoc.org/collections/view?docId=ead/Mss.530.1.Ar2-ead.xml"><em>Archive
    for the History of Quantum Mechanics</em></a>, Van Vleck said: “One always
    thinks of [quantum mechanics’] effect and successes in connection with
    spectroscopy, but I remember Niels Bohr saying that one of the great
    arguments for quantum mechanics was its success in these non-spectroscopic
    things such as magnetic and electric susceptibilities.” Van Vleck was so
    taken with this result that it figures prominently in his 1977 Nobel
    lecture.</p>

    <p>In the third paper, entitled “The intensities of the Zeeman components
    in the partial Paschen-Back effect,” Mensing returned to spectroscopy. The
    <a href="https://en.wikipedia.org/wiki/Zeeman_effect"><em>Zeeman
    effect</em></a> is the splitting of spectral lines when the atoms emitting
    light are placed in an external magnetic field. <a
    href="https://en.wikipedia.org/wiki/Pieter_Zeeman"><em>Pieter
    Zeeman</em></a> originally found a splitting in three components. Hendrik
    Antoon Lorentz could explain this on the basis of classical theory and the
    two of them shared the 1902 Nobel Prize for this work. Soon thereafter,
    however, splittings in more than three components were found. As this could
    not be explained classically, this became known as the <em>anomalous</em>
    Zeeman effect, even though it was more common than the “normal” Zeeman
    effect. An important hint to its eventual explanation in quantum mechanics
    came from the discovery by <a
    href="https://en.wikipedia.org/wiki/Friedrich_Paschen"><em>Friedrich
    Paschen</em></a> and <a
    href="https://en.wikipedia.org/wiki/Ernst_Emil_Alexander_Back"><em>Ernst
    Back</em></a> in T&uuml;bingen in 1912 that in sufficiently strong magnetic
    fields the splitting in just three components returned. This Paschen-Back
    effect thus suggested that the Zeeman effect was due partly to magnetic
    fields within the atom. Using the new concept of spin and the associated
    magnetic moment of the electron as well as the new framework of quantum
    mechanics, Heisenberg and Pauli were finally able to explain the Zeeman
    effect in terms of spin-orbit coupling. Building on their paper, Mensing
    successfully dealt with the <em>partial</em> Paschen-Back effect, i.e., the
    absence in some cases of lines in normal Zeeman triplets.</p>

    <h3>Read more on:</h3>
    <ul>
    <li><a href="/suscept">The electric susceptibility of diatomic gases</a></li>
    <li><a href="/vibrot">The rotation-vibration spectra of diatomic molecules</a></li>
    </ul>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/suscept")
def suscept():
    title = "The electric susceptibility of diatomic gases"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>The electric susceptibility of a gas is a measure of how the gas
    responds to an external electric field (similarly for magnetic
    susceptibility). Consider a gas of diatomic molecules such as HCl. Such
    molecules will have a permanent electric dipole moment, with the hydrogen
    atom the positive and the chlorine atom the negative pole. When such
    molecules are placed in an electric field, their dipole moments will try to
    align with the field. In addition, the field will move the positive and
    negative poles a little further apart. The electric susceptibility <span
    class="math inline"><em>χ</em></span> of a gas of diatomic molecules is a
    combination of these two effects. It is described by a formula proposed by
    <a href="https://en.wikipedia.org/wiki/Peter_Debye"><u>Peter Debye</u></a>
    in 1912, modeled on a similar formula proposed by <a
    href="https://en.wikipedia.org/wiki/Paul_Langevin"><u>Paul Langevin</u></a>
    for magnetic susceptibility (where only the alignment effect plays a
    role). The formula for <span class="math inline"><em>χ</em></span> thus
    became known as the Debye-Langevin formula:</p>

    <p><span class="math inline">$\chi = \ N\left( \alpha + \frac{{\mu^{{2}}}}{{3kT}}
    \right)$</span>,</p>

    <p>where <span class="math inline"><em>N</em></span> is the number of
    molecules, <span class="math inline"><em>α</em></span> is a constant, <span
    class="math inline"><em>μ</em> </span>is the permanent electric moment of
    individual molecules, <span class="math inline"><em>k</em></span> is
    Boltzmann’s constant, and <span class="math inline"><em>T</em></span> is
    the temperature.</p>

    <p>For our purposes, only the alignment effect, captured by the second term
    in the Debye-Langevin formula, is important. The alignment is frustrated by
    the thermal motion of the molecules. This is why this second term has the
    temperature in its denominator: the higher the temperature, the smaller the
    alignment effect. Put differently: the greater the energy of the molecules,
    the smaller the alignment effect. In fact, in classical theory only the
    lowest energy states contribute to <span class="math
    inline"><em>χ</em></span>.</p>

    <p>The second term of the Langevin-Debye formula can be written as</p>
    <p><span class="math inline">$\chi = \ C\frac{{{{N\mu}}^{{2}}}}{{kT}}$</span>.</p>

    <p>Classical theory correctly predicted that <span class="math inline">$C =
    \frac{{1}}{{3}}$</span>. The old quantum theory predicted a much larger
    value. Using integer quantum numbers, Mensing’s mentor <a
    href="https://en.wikipedia.org/wiki/Wolfgang_Pauli"><u>Wolfgang
    Pauli</u></a> found <span class="math inline"><em>C</em> = 1.54</span> when
    he did the calculation in 1921, almost five times the classical
    value. Unlike the situation with the spectrum of these diatomic molecules,
    half-integer quantum numbers only made matters worse. When <a
    href="https://en.wikipedia.org/wiki/Linus_Pauling"><u>Linus Pauling</u></a>
    redid Pauli’s calculation a few years later with half-integer quantum
    numbers, he found <span class="math inline"><em>C</em> = 4.57</span>,
    almost 14 times the classical value! This is the problem Pauli hoped
    Mensing could help him solve in the new quantum mechanics.</p>

    <p>The root of this problem for the old quantum theory, as with the problem
    of the spectrum of diatomic molecules, was the rule for the quantization of
    angular momentum. The calculation of the contribution of the alignment
    effect to the electric susceptibility proceeds in two steps, taking two
    different averages. First, one has to take the <em>time average</em> of the
    component of a molecule’s dipole moment in the direction of the electric
    field. Then one has to take an <em>ensemble average</em>, i.e., one has to
    average the time average of individual molecules over all molecules in the
    gas, assuming a normal (Boltzmann) distribution of these molecules over all
    states they could be in.</p>

    <p>If one does this calculation in classical mechanics <em>for all but the
    lowest energy states</em>, the time average gives an expression of the
    form</p>

    <p><span class="math inline"><em>A</em>(<em>L</em>)(3−1)</span>,</p>

    <p>where <span class="math inline"><em>L</em></span> is the length of the
    molecule’s angular momentum vector, <span class="math
    inline"><em>L</em><sub><em>z</em></sub></span> is the <span class="math
    inline"><em>z</em></span>-component of that vector, <span class="math
    inline"><em>A</em>(<em>L</em>)</span> is some combination of quantities
    which depend on <span class="math inline"><em>L</em></span>, and the
    overbar indicates the time averaging mentioned above. If we average this
    time average over all molecules, using a double bar for this ensemble
    averaging, we get</p>

    <p><span class="math inline">$= \frac{{1}}{{3}}$</span>,</p>

    <p>since <span class="math
    inline"><em>L</em><sup>2</sup> = <em>L</em><sub><em>x</em></sub><sup>2</sup> + <em>L</em><sub><em>y</em></sub><sup>2</sup> + <em>L</em><sub><em>z</em></sub><sup>2</sup></span>
    and the <span class="math inline"><em>x</em></span>- <span class="math
    inline"><em>y</em></span>- and <span class="math
    inline"><em>z</em></span>-directions will be represented equally among the
    molecules in the gas. It follows that the contribution to the alignment
    effect coming from the bulk of the molecules’ energy states vanishes. The
    only contribution comes from the lowest energy states, as one would expect,
    and it could be shown that this contribution is of just the right amount,
    with <span class="math inline">$C = \frac{{1}}{{3}}$</span>.</p>

    <p>Both in the old and in the new quantum theory, one arrives at
    expressions for the time average of the component of a molecule’s dipole
    moment in the direction of the electric field by using the quantization
    rules for angular momentum. In the old quantum theory, these rules are
    <span class="math inline">$L = l\frac{{h}}{{2\pi}}$</span> (with <span
    class="math inline"><em>l</em> = 1, 2, 3, …</span>) and <span class="math
    inline">$L_{{z}} = m\frac{{h}}{{2\pi}}$</span> (with <span class="math
    inline"><em>m</em> =  − <em>l</em>, ..., 0, 1, ..., <em>l</em></span>) and
    the time average becomes:</p>

    <p><span class="math inline">$A(L)\left( 3\frac{{m^{{2}}}}{{l^{{2}}}} - 1
    \right)$</span>.</p>

    <p>In the new quantum theory, the first of these quantization rules gets
    replaced by <span class="math inline">$L^{{2\ }} = l(l +
    1)\frac{{h^{{2}}}}{{4\pi^{{2}}}}$</span> (with <span class="math
    inline"><em>l</em> = 0, 1, 2, 3, …</span>) and the time average becomes</p>
    <p><span class="math inline">$A(L)\left( 3\frac{{m^{{2}}}}{{l(l + 1)}} - 1
    \right)$</span>.</p>

    <p>To find the contribution to the alignment effect, we need to average
    these expressions over all possible states, i.e., over all possible values
    of the quantum numbers <span class="math inline"><em>l</em></span> and
    <span class="math inline"><em>m</em></span> labeling these states. To get
    the empirically correct answer, it had better be the case that only the
    lowest energy state contributes and that the contributions of all other
    states sum to zero.</p>

    <p>In the old quantum theory, this is not the case. Since the value <span
    class="math inline"><em>l</em> = 0</span> is ruled out, the lowest energy
    state is forbidden and thus does not contribute to the alignment effect at
    all. In that sense, as Pauli pointed out when he did the calculation in
    1921, it was fortunate that the higher energy states
    contributed. Unfortunately, their contribution was almost five times too
    large. And with half-integer quantum numbers it was almost fourteen times
    too large! As <a
    href="https://en.wikipedia.org/wiki/John_Hasbrouck_Van_Vleck"><u>Van
    Vleck</u></a> said in his <a
    href="https://search.amphilsoc.org/collections/view?docId=ead/Mss.530.1.Ar2-ead.xml"><u>AHQP
    interview</u></a>, the old quantum theory produced some “wonderful
    nonsense” on this score.</p>

    <p>Mensing and Pauli took care of this “nonsense” in their 1926
    paper. First of all, the value <span class="math
    inline"><em>l</em> = 0</span> is no longer ruled out and they showed that
    this state accounts for the full alignment effect, restoring the constant
    <span class="math inline"><em>C</em></span> to its classical value of <span
    class="math inline">$\frac{{1}}{{3}}$</span>. Furthermore, they showed that the
    contributions coming from all other states are zero! This follows
    immediately from the well-known sum of squares formula. Customized to the
    situation at hand, this formula says that</p> <p><span class="math
    inline">$m^{{2}} = 2m^{{2}} = \frac{{1}}{{3}}l(l + 1)(2l + 1).$</span></p>

    <p>We can use this formula to compute the average of the time average over
    all possible values of <span class="math inline"><em>m</em></span> for a
    given value of <span class="math inline"><em>l</em></span>, the two quantum
    numbers labeling the allowed states of the system. This average, it turns
    out, vanishes for all values of <span class="math
    inline"><em>l</em> ≠ 0</span>:</p>

    <p><span class="math inline">$\frac{{1}}{{2l + 1}}\left( \frac{{3m^{{2}}}}{{l(l +
    1)}} - 1 \right) = \frac{{1}}{{2l + 1}}\left( \frac{{3m^{{2}}}}{{l(l + 1)}} - (2l + 1)
    \right) = 0\ $</span>.</p>

    <p>As Mensing and Pauli, with obvious relief, note in an italicized the
    clause in their paper: “<em>Only the molecules in the lowest state will
    therefore give a contribution to the temperature-dependent part of the
    dielectric constant</em>.”</p>

    <h3>Go back to</h3>
    <ul>
    <li><a href="/important_papers"><i>Three important papers</i></a></li>
    </ul>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/vibrot")
def vibrot():
    title = "The rotation-vibration spectra of diatomic molecules"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>In both the old and the new quantum theory, diatomic molecules, like
    carbon monoxide (CO) or hydrogen chloride (HCl), can be modeled as systems
    of two bodies connected by a spring. The system can execute both vibrations
    and rotations as indicated in the figure below.</p>

    <figure>
    <img width="300" src="static/diatomic_molecule.jpg"><br/>
    <figcaption>Model of a diatomic molecule</figcaption>
    </figure>
   
    <p>The spectrum of the light emitted by these molecules consists of a
    number of equally spaced lines in the infrared on both sides of a missing
    central line.</p>

    <figure>
    <img width="400px" src="static/diatomic_spectrum.jpg"><br/>
    <figcaption>Typical spectrum of a diatomic molecule</figcaption>
    </figure>

    <p>These spectral lines originate from transitions in which the molecule
    simultaneously changes its vibrational and rotational state. The energy gap
    between different vibrational states is much larger than the energy gap
    between different rotational states. These transitions thus give rise to
    what are called rotational bands.</p>

    <p>In both the old and the new quantum theory, the energy of diatomic
    molecules can only take on discrete values, labeled by two quantum numbers,
    <span class="math inline"><em>n</em></span> for vibrational, <span
    class="math inline"><em>l</em></span> for rotational energy:</p>

    <p><span
class="math
    inline"><em>E</em>(<em>n</em>,<em>l</em>) = <em>E</em><sub><em>v</em><em>i</em><em>b</em></sub>(<em>n</em>) + <em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>) </span>,</p>

    <p>where <span
class="math
    inline"><em>E</em><sub><em>v</em><em>i</em><em>b</em></sub>(<em>n</em>) ≫ <em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>)</span>.
The figure below shows two sets of vibrational energy levels, labeled by
    <em>n</em> and <em>n</em>+1, split into many rotational energy levels,
    labeled 0,1,2,3,…</p>

    <figure>
    <img width="400px" src="static/diatomic_levels.jpg"><br/>
    <figcaption>Energy levels of a diatomic molecule plus two allowed (blue)
    and one forbidden (red) transition between them.</figcaption>
    </figure>

    <p>The rotational energy is proportional to <span class="math
    inline"><em>L</em><sup>2</sup></span>, the angular momentum squared. The
    quantization rule for angular momentum in the old quantum is</p> <p><span
    class="math inline">$L\  = l\ \frac{{h}}{{2\pi}}$</span> with <span class="math
    inline"><em>l</em> = 1, 2, 3, …</span></p>

    <p>where <span class="math inline"><em>h</em></span> is Planck’s
    constant. So, according to the old quantum theory, the possible values of
    the rotational energy are</p>

    <p><span class="math
    inline"><em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>) = <em>C</em><em>l</em><sup>2</sup></span>
    with <span class="math inline"><em>l</em> = 1, 2, 3, …</span></p>

    <p>where <span class="math inline"><em>C</em></span> is some combination of
    <span class="math inline"><em>h</em></span>, <span class="math
    inline"><em>π</em></span>, the masses of the two molecules and the distance
    between them. For our purposes, we can treat it as a constant.</p>

    <p>Only transitions in which<span class="math inline"> <em>n</em></span>
    decreases by 1 and <span class="math inline"><em>l</em></span> increases or
    decreases by 1 are allowed. Schematically:</p>

    <p><span class="math
    inline">(<em>n</em>+1, <em>l</em>) → (<em>n</em>, <em>l</em>±1)</span></p>
    <p>The Bohr frequency condition says that the energy difference between
    initial and final state is equal to Planck’s constant times the frequency
    <span class="math
    inline"><em>ν</em><sub><em>l</em> → <em>l</em> ± 1</sub></span> of the
    light emitted in the transition:</p>

    <p><span class="math
    inline"><em>h</em><em>ν</em><sub><em>l</em> → <em>l</em> ± 1</sub> = <em>E</em>(<em>n</em>+1,<em>l</em>) − <em>E</em>(<em>n</em>,<em>l</em>±1) </span></p>

    <p><span class="math
    inline"> = <em>E</em><sub><em>v</em><em>i</em><em>b</em></sub>(<em>n</em>+1) − <em>E</em><sub><em>v</em><em>i</em><em>b</em></sub>(<em>n</em>) + <em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>) − <em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>±1) </span>.</p>

    <p>The difference in vibrational energy gives the frequency of the missing
    central line, which corresponds to the forbidden transition <span
    class="math inline"><em>l</em> → <em>l</em></span>. The difference in
    rotational energy gives the shift in frequency of the lines on both sides
    of this missing line:</p>

    <p><span class="math
    inline"><em>C</em><em>l</em><sup>2</sup> − <em>C</em>(<em>l</em>+1)<sup>2</sup><sup></sup> =  − 2<em>C</em><em>l</em>  − <em>C</em> </span>,</p>

    <p><span class="math
    inline"><em>C</em><em>l</em><sup>2</sup> − <em>C</em>(<em>l</em>−1)<sup>2</sup><sup></sup> = 2<em>C</em><em>l</em>  + <em>C</em> </span>.</p>

    <p>The old quantum theory thus predicts that the spectrum is symmetric
    around the missing line. In fact, it is shifted a little to the left. As
    physicists realized at the time, a better fit with the data is obtained if
    half-integer quantum numbers are used for angular momentum, i.e., if the
    expressions for <span class="math inline"><em>L</em></span> and <span
    class="math
    inline"><em>E</em><sub><em>r</em><em>o</em><em>t</em></sub></span>are
    replaced by:</p>

    <p><span class="math inline">$L\  = \left( l + \frac{{1}}{{2}} \right)\
    \frac{{h}}{{2\pi}}$</span>, <span class="math inline">$E_{{rot}}(l) = C\left( l +
    \frac{{1}}{{2}} \right)^{{2}}$</span>.</p>

    <p>In that case the frequency shifts are given by:</p>

    <p><span class="math inline">${{C\left( l + \frac{{1}}{{2}} \right)}}^{{2}} -
    {{{{C\left( l + \frac{{3}}{{2}} \right)}}^{{2}}}}^{{}}\  = \  - 2Cl\  - 2C\
    $</span>,</p>

    <p><span class="math inline">${{C\left( l + \frac{{1}}{{2}} \right)}}^{{2}} -
    {{{{C\left( l - \frac{{1}}{{2}} \right)}}^{{2}}}}^{{}}\  = \ 2Cl\ $</span>.</p>

    <p>So the entire spectrum is shifted <span class="math
    inline"><em>C</em>/<em>h</em></span> to the left, which is in better
    agreement with the data. Unfortunately, it was completely unclear where
    these half-integer quantum numbers were coming from.</p> <p>Mensing
    provided a simple solution to this puzzle in the course of treating the
    problem with the new quantum mechanics. The new rule for the quantization
    of angular momentum is</p>

    <p><span class="math inline">$L^{{2\ }} = l(l +
    1)\frac{{h^{{2}}}}{{4\pi^{{2}}}}$</span> <span class="math
    inline"><em>l</em> = 0, 1, 2, …</span></p>

    <p>So the rotation energy     becomes</p>

    <p><span class="math
    inline"><em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>) = <em>C</em><em>l</em>(<em>l</em>+1)</span>.</p>

    <p>We now have</p>

    <p><span class="math
    inline"><em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>) − <em>E</em><sub><em>r</em><em>o</em><em>t</em></sub>(<em>l</em>±1) = <em>C</em><em>l</em>(<em>l</em>+1) − <em>C</em>(<em>l</em>±1)(<em>l</em>±1+1) </span>,</p>

    <p>which works out to:</p>

    <p><span class="math
    inline"><em>C</em><em>l</em>(<em>l</em>+1) − <em>C</em>(<em>l</em>+1)(<em>l</em>+2) =  − 2<em>C</em><em>l</em>  − 2<em>C</em> </span>,</p>

    <p><span class="math
    inline"><em>C</em><em>l</em>(<em>l</em>+1) − <em>C</em>(<em>l</em>−1)<em>l</em> = 2<em>l</em><em>C</em></span>.</p>

    <p>This is the same result found with half-integer quantum numbers in the
    old quantum. This is not surprising given that</p>

    <p><span class="math inline">$l(l + 1) = \left( l + \frac{{1}}{{2}} \right)^{{2}}
    - \frac{{1}}{{4}}$</span></p>

    <p>(the term <span class="math inline">$\frac{{1}}{{4}}$</span> does not matter
    since only energy differences matter in the end). Mensing thus explained
    why half-integer quantum numbers had worked better in the old quantum
    theory.</p>

    <h3>Go back to</h3>
    <ul>
    <li><a href="/important_papers"><i>Three important papers</i></a></li>
    </ul>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/belated_recognition")
def belated_recognition():
    title = "Belated recognition"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <div>

    <p>
    The wikipedia page for Lucy Mensing, based largely on the article about her
    by Gernot M&uuml;nster in Physik Journal, seems to have brought her some belated
    recognition and increased visibility. Here are three examples:
    </p>

    <ol>
    <li>In 2021, the Helmholtz-Zentrum Dresden-Rossendorf announced a <a
    href="https://www.hzdr.de/db/Cms?pOid=63283&pNid=0&pLang=de">new
    development fund</a> (Förderfonds) named after Mensing to support parents,
    especially women, seeking to return to the academic work force after giving
    birth and taking care of children.</li>
    <li>In 2022, Amazon Braket launched a <a
    href="https://www.scientific-computing.com/news/amazon-braket-launches-lucy-new-quantum-processor-oxford-quantum-circuits">new
    quantum processor</a> named Lucy.</li>
    <li>In 2023, the Deutsches Museum presented an &ldquo;<a
    href="https://xrhub-bavaria.de/ar-walk-of-fame/">augmented reality walk of
    fame</a>&rdquo; for important female scientists, which includes Mensing and
    features a sculpture by Anke Schiemann entitled “Mother Lucy” (Mutter
    Lucy).</li>
    </ol>

    </div>

    </div>

    {timeline()}

    </body>
    </html>
    """

    return html


@app.route("/recollections")
def recollections():
    title = "Reminiscences"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <div>
    <p>In the 1980s, Lucy Sch&uumltz wrote down some memories of her life and career
    in several fragmentary notes. The most extensive of these is the seven-page
    document, dated January 1989, presented here in facsimile with a
    transcription and a (lightly) annotated translation.</p>
    </div>

    <br/>
    <hr/>
    <br/>

    <table>
    <tr>
    <th width="33%">Transcription (by Gernot M&uuml;nster)</th>
    <th width="33%">Facsimile</th>
    <th width="33%">Translation (by Michel Janssen)</th>
    </tr>
    <tr>
    <td>
    <pre>
    [p. 1]
    R&uuml;ckerinnerung Jan. 89
    Mein Dr. Diplom
    Hamburg 30. M&auml;rz 1925
    Die Pr&uuml;fung wurde vorverlegt, weil
    ich auf der G&ouml;ttinger Tagung &uuml;ber meine Dr.
    Arbeit vortragen sollte.
    Ich erhielt eine Pr&auml;mie von 500 M.
    Da ich das Leben bei der G&ouml;ttinger Tagung
    kennengelernt hatte (viel mehr Kontakte
    zwischen Professoren u. Studenten) [in the margin:
    Verh&auml;ltnis von Profess, Assistenten u. Studenten] benutzte
    ich das Geld (die Pr&auml;mie) f&uuml;r ein weiteres Studienjahr
    in G&ouml;ttingen, kam Ostern 1925 gerade zu der Zeit,
    als die neue Quantentheorie durch
    Heisenberg begonnen hatte. Interessante
    Zeit! in der Physik! Ich aß mit Heißenberg und Hund zu Mittag.
    Ostern 1926 zur&uuml;ck nach Hamburg, wollte ich
    mich aufs Staatsexamen vorbereiten.
    Da bekam ich ein Angebot von
    Landé, zu ihm als Assistentin zu
    kommen nach T&uuml;bingen. Er h&auml;tte

    [p. 2]
    eine Stelle durch die Notgemeinschaft
    bekommen.
    Ich fuhr darauf hin im August 1926
    nach &lt;G&ouml;ttingen&gt; T&uuml;bingen. Pauli in
    Hamburg &lt;schlug&gt; hatte mir vorgeschlagen, den Ram-
    sauer-Effekt (großer Wirkungsquer-
    schnitt der Edelgas-Atome (?!) nach der neuen
    Quantenmechanik zu berechnen.
    Die Situation in T&uuml;bingen war folgende:
    Gerlach beherrschte das Institut, hatte
    wohl etwa 25-28 Doktoranden. Sein einziger
    Assistent war Sch&uuml;tz.
    Landé als A[ußer]O[rdentlicher]-Professor hatte ein Zimmer im
    Erdge-
    schoß, in das f&uuml;r mich ein 2. Tisch
    gestellt wurde. Als gemeinsamen Raum gab [continued in the
    margin:]
    es nur das Lesezimmer neben der Bibliothek, das so klein war, daß
    gelegent-
    lich 2 japanische Studenten in Hockstellung B&uuml;cher studierten! was
    ich bestaunte!
    Dann hatte Dr. Back noch einen Arbeitsraum,
    ein ganz &uuml;bertrieben bescheidener Mensch,
    sicher &auml;lter als Gerlach,
    der sich immer bei den Studenten ent-
    schuldigte, wenn er anstatt Gerlach die Vorlesung halten mußte.
    Er hatte ein wichtiges Experiment
    [interlineated:] Paschen-Back-Effekt
    gemacht, ich glaube, auf dem Gebiet
    der Optik. Er war wohl so gehemmt,

    [p. 3]
    weil er eigentlich Jurist war, sich
    dann f&uuml;r Physik interessiert hatte
    und wohl ohne abgeschlossenes Physik-
    studium diesen Posten von Paschen
    bekam und bei Gerlach behielt.
    [In the margin:] "Paschen-Back-Effekt" erinnere ich jetzt wieder!
    Gerlach kam h&auml;ufig nach seiner Vorlesung am Vormittag
    zu Landé, um sich zu unterhalten.
    "Immer, wenn ich meine Vorlesung
    fertig machen muß", sagte L. gelegent-
    lich zu mir.
    L. schrieb an einem Buch &uuml;ber theor. Phy-
    sik, woraus ich die neueren Kapitel
    las und gelegentlich etwas dazu
    sagte oder fragte. (ist es erschienen? etwa 27/28 29?)
    Im &uuml;brigen x-te ich an meinem
    Problem. Es f&uuml;hrte auf komplizierte
    mathem. Funktionen (nicht tabuliert).
    Es war langwierige Rechenarbeit
    und f&uuml;hrte zu keinem brauchbaren
    Ergebnis. Pauli war damals in der
    Schweiz, so war es unm&ouml;glich, ihn zu besuchen
    u. Rat zu holen. - Landé verstand nichts
    von der Sache. - Warum schrieb ich nicht an Pauli???

    [p. 4]
    Der erste Zusammenstoß zwischen G[erlach] u.
    L[andé], den ich miterlebte, geschah nach einer Tagung in
    Stuttgart. G. hatte ein Taxi f&uuml;r die R&uuml;ck-
    fahrt genommen, nahm u. a. Landé
    u. mich mit. L. bat, an seiner
    Wohnung aussteigen zu d&uuml;rfen, was G wegen
    des vielen Gep&auml;cks, das noch lose im Auto lag, ablehnte.
    Es gab &auml;rgerliches hin u. her. G gab nicht
    nach. - Ob noch weitere, wesentlichere
    Differenzen vorher oder nachher vorlagen, weiß ich nicht.
    L. betrat das Inst. nicht mehr, arbeitete
    zu Hause ("kein Zustand, daß er seine
    Assistentin nicht sprechen k&ouml;nnte!"
    Anfang 28 hatte L. eine Einladung
    nach USA (f&uuml;r 1 Jahr? er vermietete
    seine Wohnung m&ouml;bliert). Ich ging
    nach Hause nach Hamb., schrieb das
    negative Ergebnis meiner Arbeit zus,
    schickte es an die Z.Sch f. Phys. Sie
    erschien im Sommer 28, gleich dahinter
    stand das gleiche Thema erfolgreich aus

    [p. 5]
    Stockholm von einem Prof mit meh-
    reren Assistenten und einer Rechenma-
    schine, und sicher mit neuer Idee &uuml;ber
    das Kraftfeld.
    &lt;Ich heirat&gt; W. Sch&uuml;tz u. ich heirateten
    im Sept. 28 im Herbst. Am n&auml;chsten Tag las
    ich in der Zeitung den Tod von W. Wien
    und sagte: "da wird Gerlach sein
    Nachfolger." Das war dann wirklich
    so, Ende 29 zogen Gerl. u. wir nach
    M&uuml;nchen. Ob u. wann Landé 29
    nach T&uuml;bingen zur&uuml;ck gekommen
    ist, erinnere ich nicht. Ich h&ouml;rte
    aber, daß er eine Berufung nach
    den USA hatte. Vielleicht hat er
    nur 1930 seinen T&uuml;binger Haushalt
    aufgel&ouml;st? u. ist wieder in die USA gefahren?
    Ich erinnere dann nur einen
    Brief \/ von ihm an meinen Mann oder einen
    anderen Physiker: "Er freue sich, daß
    wir in Deutschland jetzt alle so
    einig lebten!"
    [In the margin:]
    \/ wohl von 33[?]
    bei Tagung in Berlin

    [p. 6 (a)]
    Ich hatte schon vorher gedacht:
    "Was haben die Landés f&uuml;r ein Gl&uuml;ck
    gehabt! Sind jetzt in Land u.
    Sprache eingelebt! Die anderen
    Juden m&uuml;ssen erst eine Arbeits-
    stelle suchen u.s.w.!

    [p. 6 (b)]
    Ich denke jetzt:
    "Warum habe ich nicht die theoret.
    Physik bei Landé nochmal geh&ouml;rt?
    u. bei Born
    Ich hatte sie in Hamb. bei Lenz geh&ouml;rt,
    der frisch von Sommerfeld kam, und
    daneben bei Pauli "kinetische Gas-
    Theorie.
    Es h&auml;tte einen guten Kontakt geben
    k&ouml;nnen zwischen Landé u. mir, und sicher Anregung!
    </pre>
    </td>
    <td>
    [pp. 1-2]<br/>
    <img width="450px" src="static/page1-2.jpg"><br/>
    [pp. 3-4]<br/>
    <img width="450px" src="static/page3-4.jpg"><br/>
    [p. 5]<br/>
    <img width="450px" src="static/page5.jpg"><br/>
    [pp. 6a-6b]<br/>
    <img width="450px" src="static/page6a-6b.jpg"><br/>
    </td>
    <td>
    <p><strong>[p. 1]</strong></p>

    <p>Reminiscences, January 1989</p>

    <p>My PhD diploma: March 30, 1925</p>

    <p>The exam was moved to an earlier date because I was supposed to give
    a talk about my dissertation at the G&ouml;ttingen meeting [probably the
    meeting of a local chapter (<em>Gauverein Niedersachsen</em>) of the
    German Physical Society (<em>Deutsche Physikalische Gesellschaft</em>)
    in February 1925]</p>

    <p>I received a premium of 500 Mark. Since I had become acquainted with
    life in G&ouml;ttingen at the meeting (a lot more contact between professors and
    students [in the margin: relations between professors, assistants and
    students]), I used the prize money for an additional year of study in
    G&ouml;ttingen. I arrived at Easter 1925, right around the time that the new
    quantum theory started with Heisenberg. Interesting time! in physics! I
    used to have lunch with Heisenberg and <a
    href="https://en.wikipedia.org/wiki/Friedrich_Hund"><u>Hund</u></a>.</p>
    <p>Easter 1926, back in Hamburg, I wanted to prepare for the state exam [to
    get a teaching license].</p>

    <p>Then I got an offer from Landé to become his assistant in T&uuml;bingen. He
    had</p>

    <p><strong>[p. 2]</strong></p>

    <p>a position financed by the Emergency Association [of German Science (<a
    href="https://en.wikipedia.org/wiki/Notgemeinschaft_der_Deutschen_Wissenschaft"><u>Notgemeinschaft
    der Deutschen Wissenschaft</u></a>)].</p>

    <p>I then went to T&uuml;bingen in August 1926. In Hamburg, Pauli had suggested
    to me to calculate the Ramsauer effect (large cross section of noble gas
    atoms (?!)) using the new quantum mechanics.</p>

    <p>The situation in     T&uuml;bingen was as follows: Gerlach ruled the
    institute; he had about 25– 28     doctoral students. His only assistant
    was Sch&uuml;tz. Landé, the associate     professor, had a room on the ground
    floor, in which a second desk was placed for me. As a common room
    [continued in the margin:] there was the reading room next to the library,
    which was so small that sometimes two Japanese students studied their books
    in a squatting position! which I marveled at!</p>

    <p>Then there was some office space for Dr. Back, an overly modest person,
    definitely older than Gerlach, who would always apologize to the students
    whenever he had to give one of Gerlach’s lectures. He had done an important
    experiment, in the field of optics I believe [interlineated: Paschen–Back
    effect]. The reason he was so inhibited was probably</p>

    <p><strong>[p. 3]</strong></p>

    <p>[in the margin: “I now remember again: the Paschen–Back effect,”]</p>
    <p>that he actually was a lawyer, who had developed an interest in physics
    and, even though he had not finished his physics education, was given a
    position by Paschen, which he then kept under Gerlach.</p> <p>After his
    late morning lectures, Gerlach often came to Landé to chat: “Always right
    when I have to prepare my lectures,” Landé used to say to me.</p>

    <p>Landé was working on a book on theoretical physics, from which I read
    the newer chapters and about which I would say or ask something every once
    in a while (did it appear? 27/28 29?).</p>

    <p>Other than that, I worked on     my problem [the Ramsauer effect]. It
    led to complicated mathematical functions (not tabulated). It was a tedious
    work calculating this and it did not lead to any usable result. Pauli was
    in Switzerland at the time, so it was impossible to visit him and get his
    advice. Landé did not understand any of it. Why did I not write to
    Pauli???</p>

    <p><strong>[p. 4]</strong></p>

    <p>The first collision between G[erlach] and L[andé] that I experienced
    happened after a meet- ing in Stuttgart. G. took a taxi on the way back and
    took Landé and me, among others,49 with him. L. asked to get out at his
    place, which G. refused because of the many loose pieces of luggage still
    lying in the car. Some irritated back and forth ensued but G. did not
    relent. Whether there were any further, more substantial differences,
    earlier or later, I do not know. L. no longer set foot in the institute and
    worked from home (“Never mind that he could not talk to his assistant this
    way!”)</p>

    <p>Early 28, Landé got an invitation to the USA (for one year? he rented
    out his apartment furnished). I went home to Hamburg, wrote up the negative
    result of my work and sent it to the Zeitschrift f&uuml;r Physik. It appeared in
    summer 28, followed directly by a paper tackling the same theme
    successfully</p>

    <p>[Mensing’s paper on the Ramsauer effect actually appeared in the fall of
    1927: Lucy Mensing, “<a
    href="/omitted"><u>Zur
    Theorie des Zusammenstoßes von Atomen mit langsamen Elektronen</u></a>.”
    <em>Zeitschrift f&uuml;r Physik</em> 45 (1927) 603–609. <a
    href="https://link.springer.com/article/10.1007/BF01331923"><u>DOI</u></a>]</p>
    <p><strong>[p.5]</strong></p>

    <p>by a professor in Stockholm with several assistants and a calculating
    machine, and certainly with a new idea about the force field.</p>

    <p>[Hilding Faxén and Johan Peter Holtsmark, “<a
    href="/omitted"><u>Beitrag
    zur Theorie des Durchganges langsamer Elektronen durch Gase</u></a>.”
    <em>Zeitschrift f&uuml;r Physik</em> 45 (1927) 307–324. <a
    href="https://doi.org/10.1007/BF01343053"><u>DOI</u></a>]</p>

    <p>W. Sch&uuml;tz and I got married in September 1928 in the fall. The next day,
    I read in the paper that Wilhelm Wien had died and said: “now Gerlach will
    become his successor.” And that indeed happened. At the end of 1929,
    Gerlach and the two of us moved to Munich. Whether or when Landé returned
    to T&uuml;bingen in 1929 I don’t remember. I did hear, however, that he got a
    call to the USA. Maybe he only dissolved his household in T&uuml;bingen in 1930?
    and went back again to the USA? I only remember a letter to my husband or
    some other physicists [in the margin:] probably from 1933 at a conference
    in Berlin, saying “he was pleased that we all live in such harmony in
    Germany these days!”</p>

    <p><strong>[p. 6 (a)]</strong></p> <p>I had already thought earlier: How
    lucky for the Landés. They are al- ready accustomed to country and
    language! Other Jews still have to find a position etc.</p>

    <p><strong>[p. 6 (b)]</strong></p>

    <p>I’m now thinking: Why did I not take theoretical physics again with
    Landé? I had taken it in Hamburg, with Lenz, freshly arrived from
    Sommerfeld, [interlineated: and with Born] and also with Pauli, the kinetic
    theory of gases. It could have led to a good contact between Landé and me,
    and, for sure, inspiration!</p>

    </td>
    </tr>
    </table>


    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/early_life_edu")
def early_life_edu():
    # FYI To save the images from Michel's page, copy-paste into a libreoffice writer doc
    # and then save the image to a file from there (stupid Google).
    title = "Mensing's Early Life and Education"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>Lucy (officially: Lucy Luise Martha) Mensing was born on March 11, 1901
    in Hamburg, the first of four daughters of Hermann Mensing and his wife
    Martha Luise (née Beer). Like her mother, she attended the St. Johannis
    monastery school, known for its program to train women to become teachers
    (<em>Lehrerinnenseminar</em>). Upon graduation in 1920, she matriculated at
    the University of Hamburg, founded only the year before, to study
    physics.</p>

    <p>In addition to physics classes, she and her fellow student <a
    href="https://en.wikipedia.org/wiki/Ernst_Ising"><em>Ernst Ising</em></a>
    took a literature class, which gave them an <a
    href="/expressionism"><em>early appreciation of German expressionist
    painting</em></a>.</p>

    <p>Mensing graduated in March 1925 with a dissertation on the <a
    href="https://en.wikipedia.org/wiki/Stark_effect"><em>Stark effect</em></a>
    (the splitting of spectral lines when the atoms emitting light are placed
    in an external electric field) in the context of the old quantum
    theory. Officially, her adviser was Hamburg’s professor of theoretical
    physics, <a href="https://en.wikipedia.org/wiki/Wilhelm_Lenz"><em>Wilhelm
    Lenz</em></a>, but because of Lenz’s poor health she worked mainly with his
    assistant, <a
    href="https://en.wikipedia.org/wiki/Wolfgang_Pauli"><em>Wolfgang
    Pauli</em></a>.</p>

    </div>

    {timeline()}

    </body>
    </html>
    """

    return html


@app.route("/goettingen")
def goettingen():
    title = "Mensing's Time in G&ouml;ttingen"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>Mensing won an award for her doctorate and used the money to spend a
    year in G&ouml;ttingen. She arrived there in April 1925, right around the time
    when <a href="https://en.wikipedia.org/wiki/Max_Born"><em>Max Born</em></a>
    and his young collaborators <a
    href="https://en.wikipedia.org/wiki/Werner_Heisenberg"><em>Werner
    Heisenberg</em></a> and <a
    href="https://en.wikipedia.org/wiki/Pascual_Jordan"><em>Pascual
    Jordan</em></a> were taking the first steps toward matrix mechanics, the
    first incarnation of the new quantum mechanics.</p>

    <p>During her year in G&ouml;ttingen, she wrote <a
    href="/important_papers"><em>three important papers</em></a>, applying
    the new quantum mechanics to puzzles left unsolved by the old quantum
    theory.</p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/tuebingen")
def tuebingen():
    title = "Mensing's Time in T&uuml;bingen"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>After a successful year in G&ouml;ttingen, Mensing went back home to Hamburg,
    where she planned to take the state exam needed to get a teaching
    license. As a woman she had little to no chance of ever landing a
    professorship. Becoming a high-school teacher may have been her best bet to
    stay involved with physics.</p>

    <p>Yet she dropped this plan when <a
    href="https://en.wikipedia.org/wiki/Alfred_Landé"><em>Alfred Landé</em></a>
    offered her a one-year assistantship at the University of
    T&uuml;bingen. Unfortunately, her winning streak in G&ouml;ttingen did not continue
    in T&uuml;bingen. Not only was her research (on the <a
    href="https://en.wikipedia.org/wiki/Ramsauer–Townsend_effect"><em>Ramsauer
    effect</em></a>) not going well, she was also put off by the competitive
    mentality she encountered in the physics community. In 1928, realizing that
    this would mean the end of her career in physics, she married <a
    href="https://de.wikipedia.org/wiki/Wilhelm_Sch&uuml;tz_(Physiker)"><em>Wilhelm
    Sch&uuml;tz</em></a>, who had come to the physics institute in T&uuml;bingen as the
    assistant of <a
    href="https://en.wikipedia.org/wiki/Walther_Gerlach"><em>Walther
    Gerlach</em></a>, the successor of <a
    href="https://en.wikipedia.org/wiki/Friedrich_Paschen"><em>Friedrich
    Paschen</em></a> as director of the institute.</p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/muenchen_koenigsberg")
def muenchen_koenigsberg():
    title = "Mensing's Time in M&uuml;nchen, K&ouml;nigsberg and Jena"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>In 1929, the couple moved to Munich, where Gerlach succeeded <a
    href="https://en.wikipedia.org/wiki/Wilhelm_Wien"><em>Wilhelm
    Wien</em></a>. In 1930, Lucy Mensing, now Sch&uuml;tz, published what would turn
    out to be her <a
    href="/omitted"><em>last
    paper</em></a> and gave birth to her first child, J&uuml;rgen (1930–2018). The
    couple would have three more children: another son, Ulrich (1935–2022), and
    two daughters, Cornelie (born 1937) and Dorothea (born 1939). J&uuml;rgen and
    Ulrich both went into (medical) physics, Cornelie and Dorothea into
    pharmacy and medicine, respectively.</p>

    <p>Cornelie and Dorothea were born in K&ouml;nigsberg (now Kaliningrad), where
    Wilhelm Sch&uuml;tz was appointed professor in 1936. He replaced <a
    href="https://en.wikipedia.org/wiki/Walter_Kaufmann_(physicist)"><em>Walter
    Kaufmann</em></a>, forced into early retirement by the Nazis. In August
    1944, a bombing raid of the Royal Air Force destroyed the Sch&uuml;tzes’
    apartment and they went to Jena, where Wilhelm Sch&uuml;tz had set up a branch
    of his institute in K&ouml;nigsberg.</p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/soviet")
def soviet():
    title = "Mensing's time in the Soviet Union"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>In 1947, in operation Osoaviakhim, the Soviets rounded up about two
    thousand scientists and engineers and put them to work in the Soviet
    Union. Wilhelm Sch&uuml;tz and his family were taken to the island of <a
    href="https://en.wikipedia.org/wiki/Gorodomlya_Island"><u>Gorodomlya</u></a>
    where they were forced to stay for five years. While her husband worked for
    the Soviet rocket program, Lucy Sch&uuml;tz taught at a makeshift school for the
    children of the German families.</p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


@app.route("/jena_return")
def jena_return():
    title = "Mensing's return to Jena"
    header = generate_header(title, "/static/mensing_early.jpg")
    html = f"""
    {header}

    <body>

    <div>
    <h1>{title}</h1>
    <br/><br/><br/><br/>

    <p>In 1952, the Sch&uuml;tzes were allowed to leave the Soviet Union and
    returned to Jena, now part of the new German Democratic Republic. Wilhelm
    Sch&uuml;tz got a chair in experimental physics, which he held until his
    retirement in 1965. Lucy Sch&uuml;tz would assist her husband in his work, for
    instance, by helping him prepare lecture notes. </p>

    <p>Some years after her husband’s death in 1972, Lucy Sch&uuml;tz wrote down
    some <a href="/recollections"><em>fragmentary recollections</em></a> of her
    short career in physics in the 1920s. Oddly, she didn’t write much about
    her extremely successful year in G&ouml;ttingen, focusing instead on the
    frustrating year in T&uuml;bingen that followed.</p>

    <p>In 1992, Lucy Sch&uuml;tz moved from Jena to Meiningen to be close to her
    oldest daughter, Cornelie. This is where she died three years later, on
    April 28, 1995. Her papers, which are now with her youngest daughter,
    Dorothea, will eventually be deposited in the Archives of the University of
    Jena.</p>

    </div>

    {timeline()}

    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run()
