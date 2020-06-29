from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('personal section')


class AlbumSection(Section):
    def describe(self):
        print('album section')


class PatentSection(Section):
    def describe(self):
        print('patent section')


class PublicationSection(Section):
    def describe(self):
        print('publication section')


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.create_profile()
        self._sections = list()

    @abstractmethod
    def create_profile(self):
        pass

    @property
    def sections(self):
        return self._sections

    @sections.setter
    def sections(self, section):
        self._add_section(section)

    def _add_section(self, section):
        self._sections.append(section)


class Linkedin(Profile):
    def create_profile(self):
        self.sections = (PersonalSection(), PatentSection(), PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.sections = (PersonalSection(), AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
