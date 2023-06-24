import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QProgressBar,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QMessageBox,
)


class YouTubeDownloaderUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setFixedSize(400, 200)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)
        layout.setSpacing(10)

        url_label = QLabel("YouTube URL:")
        layout.addWidget(url_label)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        self.progress_label = QLabel()
        layout.addWidget(self.progress_label)

        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)
        button_layout.setSpacing(10)

        self.playlist_button = QPushButton("Download Playlist")
        self.playlist_button.clicked.connect(self.download_playlist)
        button_layout.addWidget(self.playlist_button)

        self.video_button = QPushButton("Download Video")
        self.video_button.clicked.connect(self.download_video)
        button_layout.addWidget(self.video_button)

        layout.addWidget(button_widget)

    def download_playlist(self):
        url = self.url_input.text()
        # Add code to download the playlist
        self.show_status("Downloading playlist: " + url)
        self.show_progress_bar()

        # Simulating progress update
        self.update_progress(50)

        # Simulating completion
        self.show_status("Playlist download complete: " + url)
        self.clear_progress_bar()
        QMessageBox.information(self, "Download Complete", "Playlist download is complete.")

    def download_video(self):
        url = self.url_input.text()
        # Add code to download the video
        self.show_status("Downloading video: " + url)
        self.show_progress_bar()

        # Simulating progress update
        self.update_progress(30)

        # Simulating completion
        self.show_status("Video download complete: " + url)
        self.clear_progress_bar()
        QMessageBox.information(self, "Download Complete", "Video download is complete.")

    def show_progress_bar(self):
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(True)
        self.progress_label.setVisible(True)

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        self.progress_label.setText(f"Progress: {value}%")

    def clear_progress_bar(self):
        self.progress_bar.setVisible(False)
        self.progress_label.setVisible(False)

    def show_status(self, message):
        self.statusBar().showMessage(message)

    def clear_status(self):
        self.statusBar().clearMessage()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloaderUI()
    window.show()
    sys.exit(app.exec_())
