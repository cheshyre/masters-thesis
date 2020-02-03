# Matthias Heinz: Master's thesis

This repository will contain my Master's proposal and thesis and the slides for both defenses.
Once the actual topic is clear, I will update this to include the proper title
and a minimal abstract in the README.

## Versioning system

I am testing out a private/public 2 repository system,
which will allow me to develop quickly on the private repository,
keeping the full commit history for obvious reasons,
while updating a public repository with large-scale changes.
I will attempt to use [a variant of semantic versioning for documents](https://semverdoc.org/)
(see also the original [semantic versioning](https://semver.org/))
to keep track of versions for the documents.
The repository will be given a version number with 3 integers, MAJOR.MINOR.PATCH.
Before submission of the defense version the documents,
the version number changes should be interpreted as follows:

1. The MAJOR version number will be incremented when
   the document has reached defense version.
2. The MINOR version number will be incremented when
   the structure of the content has been changed
   (addition or removal of sections or subsections).
3. The PATCH version number will be incremented when
   fleshing out content in sections or fixing typos.

After the defense, the version number changes should be interpreted as follows:

1. The MAJOR version number will be incremented when
   a major claim made in the document has been shown to be incorrect.
   It is unlikely that the documents will be rewritten,
   but in the (hopefully unlikely) case that this happens
   I will include warnings at the beginning of incorrect sections and on the affected slides.
2. The MINOR version number will be incremented when
   the content of the documents has changed in some way that
   is not a simple typo but also does not invalidate the main claims of the thesis.
3. The PATCH version number will be incremented when
   typos are fixed.
   In most cases typos in equations will fall under this versioning classification when fixed.
   The exception to this will be formulas that are central to the document
   and are not generally available for cross-referencing in other literature.

**Summary**: This means each document will reach version 1.0.0 at the time of the defense.
Version numbers beyond that mean that I was made aware of typos or errors in my work.
A version number `>=2.0.0` indicates that something was significantly wrong,
most likely making the documents not worth reading.

