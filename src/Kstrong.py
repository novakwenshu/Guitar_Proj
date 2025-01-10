import numpy as np
import simpleaudio as sa

def karplus_strong(frequency, duration, sampling_rate=44100):
    """Generates a sound using the Karplus-Strong algorithm."""

    # Calculate the period of the waveform
    period = int(sampling_rate / frequency)

    # Create a buffer filled with random noise
    wavetable = np.random.uniform(-1, 1, period)

    # Initialize the output buffer
    output = []

    # Generate the sound
    for i in range(int(sampling_rate * duration)):
        output.append(wavetable[i % period])

        # Apply the averaging filter
        wavetable[i % period] = 0.5 * (wavetable[i % period] + wavetable[(i + 1) % period])

    # Normalize the output
    output = np.array(output)
    output = output / np.max(np.abs(output))

    # Convert the output to 16-bit audio
    audio = (output * 32767).astype(np.int16)

    return audio

# Generate a sound at 440 Hz for 2 seconds
audio = karplus_strong(440, 2)

# Play the sound
play_obj = sa.play_buffer(audio, 1, 2, 44100)
play_obj.wait_done()