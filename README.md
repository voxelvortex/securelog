# Securelog

## Intro

Pseudocrates is an AI chatbot that serves as a conversational philosophical guide developed to assist users in understanding and applying ethical reasoning to complex scenarios. The chatbot allows users to step into specific roles—such as historical or philosophical figures—and use established concepts and methods to argue, reason, and respond to ethical dilemmas or scenarios. The chatbot's primary educational goal is to immerse participants in ethical decision-making, encourage critical thinking, and help users understand and apply philosophical principles. Due to the possibility of the AI having access to a user's bio and any other potential PII information the user may type in the chat, securing that information is essential. 
The goal of this project is to prototype and integrate an adaptive, secure storage solution that stores user prompts and responses from the AI model. The proper implementation of such a system requires the creation of an anonymization module to anonymize user prompts, identify compliance requirements facing a business using generative AI, and assess the prototyped system to identify and tackle different risks, such as PII leakage, and controls that should be put in place to improve the security of the application. 
Encryption in transit is facilitated natively by Django, since REST calls are secured using TLS, which provides confidentiality and integrity guarantees, through industry-standard protocols. Additionally, using TLS allows maximum compatibility since the client (Pseudocrates) and server (Logging System) negotiate to the most secure methods and ciphers automatically. TLS makes use of certificates signed by Certificate Authorities (CAs), which allow clients to verify the integrity and identity of upstream servers, and protects against Man-in-the-Middle attacks. Methods like Ephemeral Key Exchanges provide resistance to store now decrypt later attacks, since the compromise of a single session key doesn't impact the confidentiality of other sessions.
Due to the variable nature of chatbot conversations, static anonymization methods are not sufficient in the case that a user discloses PII in their prompt, or if the model returns PII in its response. For these reasons, the use of Named Entity Recognition (NER) is beneficial. NER uses a model, trained on natural language, to scan through tokenized strings, and categorize named entities (i.e. Names, Products, Organizations, Dates). The anonymization module uses a NER to substitute named entities with a placeholder; for example a name would be substituted for “[NAME]”.

## Usage

To use Securelog, install python requirements using `pip -r requirements.txt`
\\TODO
