# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Name: MusicSongReco 1.5

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

The Recommender basically as it is named, recommends songs from a catalog, that being the cvs file, that best matches a User's musical preference. It is used by user's who wants to experience other songs that they like or have a shared taste and vibe.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The Scoring System basically has signals to garner points. It first goes through categorial matches, that being Genre and Mood in which both have weights depending on its importance. Then it goes to the closeness of other the attributes, that being energy, valance, and such. The point is decided whether it perfectly matches or not. Then it adds up the total score and ranks them.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The Dataset used is the csv file in which contains now 22 songs (added by me), where it has 10 attributes, that being [id], [title], [artist], [genre], [mood], [emergy], [tempo_bpm], [danceability], and [acousticness]. [Genre] represents pop, lofi, rock and such. [Moods] represents happy, chill, intense, and such.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

In the system, it works well on a user profile that has a well represented attributes like [High-Energy-Pop] where the user's preference being matched with multiple attributes at once.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

- A weakness that is discovered in the experiments is that the signal that matches the genre is rendered useless. Reason being is by how it over relies on the genre signal in which the csv data set. An example of it would be how for the "Deep-Intense-Rock" profile wants a Rock typed of Genre, where in the cvs file, only has one rock song. This causes the genre to not have a variaty or diverse.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

- The Profiles I tested are the given Profiles, that being [High-Energy-Pop], [Chill-Lofi], and [Deep-Intense-Rock]. 

- For [High-Energy-Pop], I look to see if the Songs are of High-Energy, Pop and such. The results gave me "Sunrise City". For [Chill-Lofi], I look for Low-Energy like "Liberty Rain". And [Deep-Intense-Rock] in which I look for "Storm RUnner".

- What suprised me the number one ranked song for [Chill-Lofi]. It seems that the Mood is Sad instead of Chill or Calm. Probably due to how the favorite mood for the Profile is skipped.

And for some reason, 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

1. Basically improving the state of my Program. The functions being more "functionality".
2. Improving the Structure. I work well in a organized structure.
3. Being able to implement handling contraints and ohter factors.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

In my experience, the recommender system is one of the interesting projects I've ever worked on. It's one of the few projects where I'm hoping to improve on more. Adding more, the fact that there are factors that may affect the scoring system such as not having enough data, or another word for a genre, mood or mixed mood and such. In my opinion, I feel like this project is more like "internship" like vibe because I figured that something like this would be a work in that area.