import flet as ft
import flet_audio as fta


def main(page: ft.Page):
    page.title = "Music Player"
    page.assets_dir = "assets"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    music_list = [
        {
            "src": "audio/DMC.mp3",
            "title": "Devils Never Cry",
            "artist": "Capcom Sound Team",
            "album": "DMC 3"
        },
        {
            "src": "audio/DMC_V.mp3",
            "title": "Bury the Light",
            "artist": "Casey Edwards",
            "album": "DMC 5"
        },
        {
            "src": "audio/Hammer.mp3",
            "title": "Hammer of Justice",
            "artist": "Toby Fox",
            "album": "Deltarune Chapter 3-4"
        },
        {
            "src": "audio/Sonic_UNLD.mp3",
            "title": "Windmill Isle Day",
            "artist": "Sega Sound Team",
            "album": "Sonic Unleashed"
        },
        {
            "src": "audio/Tidal.mp3",
            "title": "Tidal Wave",
            "artist": "Shiawase (VIP)",
            "album": "No Album"
        }
    ]

    current_song = 0
    is_playing = False

    music = fta.Audio(
        src=music_list[current_song]["src"],
        autoplay=False,
        volume=1.0
    )
    page.services.append(music)
    title_text = ft.Text(size=20, weight=ft.FontWeight.BOLD)
    artist_text = ft.Text(size=16)
    album_text = ft.Text(size=14)

    def update_song_info():
        title_text.value = f"Title: {music_list[current_song]['title']}"
        artist_text.value = f"Artist: {music_list[current_song]['artist']}"
        album_text.value = f"Album: {music_list[current_song]['album']}"

    async def play_pause(e):
        nonlocal is_playing

        if is_playing:
            play_button.icon = ft.Icons.PLAY_ARROW
            is_playing = not is_playing
            await music.pause()
        else:
            music.update()
            play_button.icon = ft.Icons.PAUSE
            is_playing = not is_playing
            await music.play()

       
    async def next_song(e):
        nonlocal current_song, is_playing

        current_song = (current_song + 1) % len(music_list)
        music.src = music_list[current_song]["src"]
        music.update()
        await music.play()

        is_playing = True
        play_button.icon = ft.Icons.PAUSE

        update_song_info()
       
    async def prev_song(e):
        nonlocal current_song, is_playing

        current_song = (current_song - 1) % len(music_list)
        music.src = music_list[current_song]["src"]
        music.update()
        music.play()

        is_playing = True
        play_button.icon = ft.Icons.PAUSE

        update_song_info()
       
    prev_button = ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS, on_click=prev_song)
    play_button = ft.IconButton(icon=ft.Icons.PLAY_ARROW, on_click=play_pause)
    next_button = ft.IconButton(icon=ft.Icons.SKIP_NEXT, on_click=next_song)

    update_song_info()

    page.add(
        ft.Column(
            [
                title_text,
                artist_text,
                album_text,
                ft.Row(
                    [prev_button, play_button, next_button],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.run(main=main, assets_dir="assets")