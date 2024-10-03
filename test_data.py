import requests

url = 'http://127.0.0.1:8000/log/api/events/'
headers = {'Content-Type': 'application/json'}
data = [
    {
        "event": "UserLogin",
        "time": "2024-09-27T08:32:00Z",
        "username": "thinker123",
        "password": "deepThoughts2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T09:00:00Z",
        "username": "thinker123",
        "name": "Plato Lover",
        "bio": "Philosophy student interested in metaphysics",
        "prompt": "My name is Plato Lover, and I am a philosophy student interested in metaphysics. What is the nature of reality, and how do we perceive it?",
        "response": "The nature of reality has been debated for centuries. Some argue for materialism, where reality is grounded in physical objects, while others advocate for idealism, suggesting that reality is shaped by the mind."
    },
    {
        "event": "UserRegister",
        "time": "2024-09-27T09:15:00Z",
        "username": "stoicSage",
        "password": "meditationAndStoicism"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T10:10:00Z",
        "username": "stoicSage",
        "name": "Marcus",
        "bio": "Practitioner of Stoic philosophy",
        "prompt": "Hello, I am Marcus, a practitioner of Stoic philosophy. How can one cultivate inner peace in a world full of distractions?",
        "response": "According to Stoicism, inner peace can be achieved by accepting things we cannot control, focusing on our own actions and reactions, and practicing virtues like wisdom, courage, and temperance."
    },
    {
        "event": "UserLogin",
        "time": "2024-09-27T10:30:00Z",
        "username": "existentialTruth",
        "password": "existence2024!"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T11:00:00Z",
        "username": "existentialTruth",
        "name": "Søren Kierkegaard",
        "bio": "Existential philosopher questioning life's purpose",
        "prompt": "Hi, my name is Søren Kierkegaard. As an existential philosopher questioning life’s purpose, why do human beings search for meaning in a seemingly indifferent universe?",
        "response": "Existentialists like Kierkegaard and Sartre argue that humans are free to create their own meaning in a world without inherent purpose. This freedom, while liberating, also carries the burden of responsibility."
    },
    {
        "event": "UserRegister",
        "time": "2024-09-27T11:30:00Z",
        "username": "nihilist456",
        "password": "nihilismIsLife"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T12:00:00Z",
        "username": "nihilist456",
        "name": "Friedrich Nietzsche",
        "bio": "Nihilist fascinated by the rejection of absolute truths",
        "prompt": "Hey, I’m Friedrich Nietzsche, a nihilist fascinated by the rejection of absolute truths. If there is no inherent meaning to life, why should one strive for greatness?",
        "response": "Nietzsche believed in the concept of the Übermensch, where individuals could create their own values and meaning. Even without inherent meaning, striving for greatness is an act of self-creation."
    },
    {
        "event": "UserLogin",
        "time": "2024-09-27T12:30:00Z",
        "username": "dualismDebater",
        "password": "mindAndBody2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T13:00:00Z",
        "username": "dualismDebater",
        "name": "Descartes Disciple",
        "bio": "Philosopher interested in dualism and the mind-body problem",
        "prompt": "Hi, I’m Descartes Disciple, a philosopher interested in dualism and the mind-body problem. How do we know the mind is separate from the body?",
        "response": "René Descartes argued for dualism, positing that the mind and body are separate entities. His famous quote 'I think, therefore I am' suggests that the mind’s existence is certain, even if the body’s isn’t."
    },
    {
        "event": "UserRegister",
        "time": "2024-09-27T13:30:00Z",
        "username": "utilitarianThinker",
        "password": "greatestGood2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T14:00:00Z",
        "username": "utilitarianThinker",
        "name": "John Stuart Mill Fan",
        "bio": "Student of utilitarian ethics",
        "prompt": "Hello, I am John Stuart Mill Fan, a student of utilitarian ethics. Is it morally justified to sacrifice one life to save many?",
        "response": "In utilitarian ethics, the morally correct action is the one that maximizes overall happiness or well-being. Sacrificing one life to save many may be justified if it leads to the greatest good for the greatest number."
    },
    {
        "event": "UserLogin",
        "time": "2024-09-27T14:30:00Z",
        "username": "deterministThinker",
        "password": "freeWillVsDeterminism"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T15:00:00Z",
        "username": "deterministThinker",
        "name": "Baruch Spinoza",
        "bio": "Philosopher exploring determinism and free will",
        "prompt": "Hi, my name is Baruch Spinoza. I’m a philosopher exploring determinism and free will. If everything is determined by prior causes, do we have any real choice in our actions?",
        "response": "Determinists argue that every event, including human actions, is the result of preceding causes. However, compatibilists suggest that free will can exist within a deterministic framework, as long as individuals act according to their own desires."
    },
    {
        "event": "UserRegister",
        "time": "2024-09-27T15:30:00Z",
        "username": "phenomenonSeeker",
        "password": "perceptionIsReality2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T16:00:00Z",
        "username": "phenomenonSeeker",
        "name": "Edmund Husserl",
        "bio": "Phenomenologist studying consciousness and experience",
        "prompt": "Hi, I’m Edmund Husserl, a phenomenologist studying consciousness and experience. How can we differentiate between subjective experience and objective reality?",
        "response": "Phenomenology seeks to study structures of consciousness from a first-person perspective. While subjective experiences are unique to the individual, objective reality is often regarded as the shared world we all interact with."
    },
    {
        "event": "UserLogin",
        "time": "2024-09-27T16:30:00Z",
        "username": "altruisticPhilosopher",
        "password": "moralGood2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T17:00:00Z",
        "username": "altruisticPhilosopher",
        "name": "Immanuel Kant Admirer",
        "bio": "Philosophy enthusiast focused on deontological ethics",
        "prompt": "Hi, I’m Immanuel Kant Admirer, a philosophy enthusiast focused on deontological ethics. Is it ever morally right to lie, even with good intentions?",
        "response": "According to Kantian ethics, lying is always morally wrong because it violates the categorical imperative, which demands that actions be universally applicable. Lying undermines trust and treats people as a means to an end."
    },
    {
        "event": "UserRegister",
        "time": "2024-09-27T17:30:00Z",
        "username": "epicureanSeeker",
        "password": "pleasureIsKey2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T18:00:00Z",
        "username": "epicureanSeeker",
        "name": "Epicurus Devotee",
        "bio": "Follower of Epicurean philosophy",
        "prompt": "Hello, I’m Epicurus Devotee, a follower of Epicurean philosophy. How should one live to achieve the highest level of happiness?",
        "response": "Epicurus believed that happiness is achieved through the pursuit of modest pleasures, intellectual fulfillment, and the absence of pain. He advocated for simple living, friendship, and self-reflection as key to happiness."
    },
    {
        "event": "UserLogin",
        "time": "2024-09-27T18:30:00Z",
        "username": "postModernist2024",
        "password": "whatIsTruth2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T19:00:00Z",
        "username": "postModernist2024",
        "name": "Foucault Follower",
        "bio": "Postmodernist thinker questioning truth and power",
        "prompt": "Hi, I’m Foucault Follower, a postmodernist thinker questioning truth and power. How is knowledge used as a tool for power in society?",
        "response": "Michel Foucault argued that knowledge and power are intertwined, with those in power shaping what is accepted as truth. Institutions like education, healthcare, and the law are key mechanisms for exerting control through knowledge."
    },
    {
        "event": "UserRegister",
        "time": "2024-09-27T19:30:00Z",
        "username": "absurdistExistentialist",
        "password": "lifeIsAbsurd2024"
    },
    {
        "event": "Chat",
        "time": "2024-09-27T20:00:00Z",
        "username": "absurdistExistentialist",
        "name": "Albert Camus Fan",
        "bio": "Existential philosopher exploring absurdism",
        "prompt": "Hi, I’m Albert Camus Fan, an existential philosopher exploring absurdism. If life is inherently meaningless, how should we respond to this absurdity?",
        "response": "Camus suggested that we should embrace the absurdity of life and continue living authentically despite it. By recognizing life’s lack of inherent meaning, we gain the freedom to create our own purpose and live passionately."
    }
]



for event in data:
    response = requests.post(url, json=event, headers=headers)
    print(f'{response.status_code}: {repr(response.json)}')

