from flask import Flask
import webbrowser as web

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Snakepedia</title>
  <link href="https://cdn.jsdelivr.net/npm/remixicon/fonts/remixicon.css" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
  <style>
    * {
      font-family: "Poppins";
      font-weight: 200;
      text-align: center;
    }
    .tworem {
      font-size: 2rem;
    }
    i {
      margin: 0 5px;
    }
    a {
      text-decoration: 0;
      color: black;
    }
    body {
      margin: 0;
      padding: 0;
    }
    .article {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      position: relative;
    }
    h2 {
      text-align: center;
      font-weight: 300;
    }
    h1 {
      text-align: center;
      font-weight: 400;
    }
    .article-content {
      border: 1px solid #999999;
      margin-top: 15px;
      padding: 15px;
    }
    img {
      display: block;
      margin: 0 auto;
      width: 100%;
      height: auto;
    }
    .heart-icon {
      position: absolute;
      bottom: 25px;
      right: 30px;
    }
    .ri-heart-fill {
      color: #eaeaea;
      font-size: 1.5rem;
    }
  </style>
</head>
<body>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const heartIcons = document.querySelectorAll('.ri-heart-fill');

      heartIcons.forEach(icon => {
        icon.addEventListener('click', function() {
          const computedColor = window.getComputedStyle(icon).color;

          if (computedColor === 'rgb(234, 234, 234)' || computedColor === '') {
            icon.style.color = 'red';
          } else {
            icon.style.color = '#eaeaea';
          }
        });
      });
    });
  </script>

  <div class="article">
    <h1>Snakepedia</h1>
    <h2>Python Snake: Nature's Impressive Constrictor</h2>
    <div class="article-content">
      <img src="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTYnS7Y1iWN_tZAgXvrcX8lwZaIdftjcps1Szmx_ZBnanr77vTbl9k8t2SdR6DqR7PxnDNJXjS-G3X_HR8" loading="lazy" alt="Python Snake">
      <p>Pythons, with their massive size and striking patterns, are renowned for their constricting prowess. Found in tropical regions worldwide, these non-venomous serpents use sheer strength to overpower prey ranging from rodents to small deer.</p>
    </div>
    <div class="heart-icon">
      <i class="ri-heart-fill"></i>
    </div>
  </div>

  <div class="article">
    <h2>Anaconda Snake: Amazon's Aquatic Titan</h2>
    <div class="article-content">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTewsij-KoQrlT4FptWXEuNr42cDwdw1PyXWg&usqp=CAU" loading="lazy" alt="Anaconda Snake">
      <p>The anaconda, a giant of the Amazon, is a formidable predator lurking in swamps and waterways. With lengths exceeding 30 feet, these aquatic serpents ambush prey like fish and caimans with remarkable speed and power.</p>
    </div>
    <div class="heart-icon">
      <i class="ri-heart-fill"></i>
    </div>
  </div>

  <div class="article">
    <h2>Black Mamba: Africa's Deadly Sprinter</h2>
    <div class="article-content">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeNo_r4mbHoIXxzD81tgrLe5LGoTC4kGbJSg&usqp=CAU" loading="lazy" alt="Black Mamba">
      <p>The black mamba, known for its lethal venom and lightning speed, is one of Africa's most feared snakes. Capable of reaching speeds of up to 12 miles per hour, encounters with these agile predators can be deadly, emphasizing the importance of caution and respect for their territory.</p>
    </div>
    <div class="heart-icon">
      <i class="ri-heart-fill"></i>
    </div>
  </div>

  <div class="article">
    <h2>Reticulated Python: Southeast Asia's Serpent Giant</h2>
    <div class="article-content">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsaBvioI573zFg6P8lOGvwWn7VK6Gb8eIXAA&usqp=CAU" loading="lazy" alt="Reticulated Python">
      <p>The reticulated python, native to Southeast Asia, is one of the longest snakes in the world. With intricate patterns adorning its scales, this python is a master of camouflage and ambush hunting, preying on mammals and birds in its habitat.</p>
    </div>
    <div class="heart-icon">
      <i class="ri-heart-fill"></i>
    </div>
  </div>

  <div class="article">
    <h2>King Cobra: Asia's Venomous Sovereign</h2>
    <div class="article-content">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-ek9jCdEYF7dhjO4xUKEzi2R-YkPgSqKYfw&usqp=CAU" loading="lazy" alt="King Cobra">
      <p>The king cobra, revered and feared in Asia, is the world's longest venomous snake. With its distinctive hood and potent neurotoxic venom, this serpent commands respect in its ecosystem, preying on other snakes and small mammals.</p>
    </div>
    <div class="heart-icon">
      <i class="ri-heart-fill"></i>
    </div>
  </div>

  <div class="article">
  <h2>Boa Constrictor: South America's Mighty Squeeze</h2>
  <div class="article-content">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTa8hsJunSwYS3hXI8Ep4bgmKnF-rOozxcS8w&usqp=CAU" loading="lazy" alt="Boa Constrictor">
    <p>The boa constrictor, with its muscular body and impressive length, is a master of constriction. Native to South America, these powerful serpents wrap around their prey and suffocate them before devouring them whole, showcasing nature's remarkable adaptation for survival.</p>
  </div>
  <div class="heart-icon">
    <i class="ri-heart-fill"></i>
  </div>
</div>

<div class="article">
  <h2>Green Tree Python: Arboreal Beauty of Oceania</h2>
  <div class="article-content">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKVkZyD3eNqbnbc4mQYoELyHq2moz06oQnCw&usqp=CAU" loading="lazy" alt="Green Tree Python">
    <p>The green tree python, with its vibrant green coloration and prehensile tail, is a sight to behold in the tropical forests of Oceania. These arboreal serpents coil around branches, patiently waiting for prey to pass by, showcasing nature's elegance and adaptability in the canopy.</p>
  </div>
  <div class="heart-icon">
    <i class="ri-heart-fill"></i>
  </div>
</div>
<div class="article">
  <h2>Coral Snake: Colorful but Deadly</h2>
  <div class="article-content">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_tGBgD6I2B4kjluvNagyaspob_ZOEIfW7hg&usqp=CAU" loading="lazy" alt="Coral Snake">
    <p>The coral snake, with its vibrant bands of red, yellow, and black, is a venomous serpent found in various regions of the Americas. Despite its striking appearance, it's not aggressive but should be avoided due to its potent neurotoxic venom.</p>
  </div>
  <div class="heart-icon">
    <i class="ri-heart-fill"></i>
  </div>
</div>

<div class="article">
  <h2>Rattlesnake: Iconic Symbol of the American West</h2>
  <div class="article-content">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREfNAU5s0zyBNqsRBs0iSeg4b6zV47tHYFrg&usqp=CAU" loading="lazy" alt="Rattlesnake">
    <p>Rattlesnakes, with their distinctive rattle and venomous bite, are emblematic of the American West. Found in a variety of habitats, from deserts to forests, these pit vipers play a crucial role in ecosystem balance despite their fearsome reputation.</p>
  </div>
  <div class="heart-icon">
    <i class="ri-heart-fill"></i>
  </div>
</div>
<hr>
<p>Follow us on:</p>
<a href="https://www.tiktok.com/@anas.web.designer?_t=8lwMG6sWH8o&_r=1"><i class="tworem ri-tiktok-fill"> </i></a> 
<a href="https://youtube.com/@AnasMostafa12?si=XngsTAYi6Jue3vZP"><i class="tworem ri-youtube-fill"> </i> </a>
<i class="tworem ri-github-fill"> </i> 
</body>
</html>
"""
@app.route('/')
def index():
    return html

web.open("http://127.0.0.1:5000")
app.run(debug=True, port=5000)
