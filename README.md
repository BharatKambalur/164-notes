
<p align="right">
<i>Do what I do. Hold tight and pretend it's a plan.</i><br>
- The Doctor - 
</p>


## Introduction
In spring 2018, I was fortunate to serve as a teaching assistant for PHYS164: an observational astronomy lab taught by professor Shelley Wright at University of California San Diego. Specifically, I was tasked to handle the computational component of the course, requiring the students to code basic astronomical routines often from first principles. Starting with the fundamentals of computer programming as a whole, we navigated our way through FITS file analysis, photometry, single-slit spectroscopy, source extraction, plate solutions, catalogue queries, astronomical coordinates and much more.
This resulted in me generating a considerable amount of notes and heavily annotated programs currently stored in this GitHub repository. While everything published here is my own work, most of it was inspired by professor Wright's lectures and produced with her help. I must also give due credit to the wonderful class of spring 2018 who guided me with feedback and questions.
## System requirements
All notes and code are presented as standalone Jupyter notebooks and are designed to run under the default Anaconda setup. Early sessions require NumPy, SciPy, MatPlotLib and AstroPy, which are likely to be present in most Anaconda distributions. Later notebooks partly rely on IPyWidgets, AstroQuery and PhotUtils with detailed installation requirements provided as necessary.
All notebooks have been tested on Python 2.7 under Windows; however, I tried to remain Python version and operating system agnostic to the best of my ability by scattering many comments throughout the notebooks emphasizing the differences between environments that are hopefully sufficient to port the code.
The introductory session is an exception to the above requirements, as it is assumed that the students will not have set up their environments in time. The notes from this session are contained in a PDF file, detailing the installation procedure. The code from those notes is presented separately as a text file.
## Data files
Some of the notebooks rely on data from University of California Observatories that are proprietary and cannot be shared here. Those notebooks are marked with a comment and will not run as they are. It is my hope that the content is general enough to be easily adapted to similar datasets. Furthermore, all notebooks are provided with their original cell output, which means that the reader should be able to follow most of them without execution.
## Note to students
During my teaching assistantship, I have been "accused" multiple times of being a little more explicit in my notes than necessary and giving too much away. This however only applies to those students who attempt to complete their assignments by blindingly copying the code and slightly tuning it to fit their purposes. As such, I feel compelled to emphasize that the code provided in this repository is only meant to serve as an example and inspire ideas. It should not at any circumstances be considered a template that can be copied and filled in. Doing so fails to prove one's understanding of the material, which is what students are assessed for. But even more importantly, this practice prevents students from seeing how the code can be improved and scaled to the situation at hand, which tends to result in lower grades even before any copying penalties are applied.
If you are a student attending PHYS 164 or a similar course, I ask of you to be responsible when using this repository and avoid falling for the dangerous misconception that this course can be completed without investing a significant amount of effort and creativity.
## Note to teachers
While I would certainly appreciate a shout-out and increased attention to my GitHub, any of the materials in this repository can be reused for any purposes with or without modification with no attribution required or expected.
In exchange, I will require all users to carefully double-check anything they choose to adopt, as my notes are nothing more than a snapshot of my understanding of the subject, which may very well be incomplete and at times outright wrong and misleading. Proceed at your own risk!
