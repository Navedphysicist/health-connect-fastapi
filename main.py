from fastapi import FastAPI
app = FastAPI()

doctors_data =  [
  {
    "about": "Dr. James is dedicated to providing high-quality healthcare with a focus on preventative care and early diagnosis.",
    "address": {
      "line1": "24 Main Street",
      "line2": "10 Clause Road"
    },
    "available": True,
    "degree": "MBBS",
    "experience": "4 Years",
    "fees": 50,
    "id": 1,
    "image": "https://mighty.tools/mockmind-api/content/human/65.jpg",
    "name": "Dr. Richard James",
    "speciality": {
      "icon": "faHeartPulse",
      "title": "Cardiology"
    }
  },
  {
    "about": "Dr. White specializes in cardiovascular health and is committed to patient education and prevention.",
    "address": {
      "line1": "100 Health Blvd",
      "line2": "Suite 20"
    },
    "available": True,
    "degree": "MD, Cardiology",
    "experience": "8 Years",
    "fees": 75,
    "id": 2,
    "image": "https://mighty.tools/mockmind-api/content/human/44.jpg",
    "name": "Dr. Sarah White",
    "speciality": {
      "icon": "faUserMd",
      "title": "Urology"
    }
  },
  {
    "about": "Dr. Brown is an expert in skin care, specializing in treatments for common and complex skin issues.",
    "address": {
      "line1": "50 Maple Ave",
      "line2": "2nd Floor"
    },
    "available": False,
    "degree": "MD, Dermatology",
    "experience": "6 Years",
    "fees": 60,
    "id": 3,
    "image": "https://mighty.tools/mockmind-api/content/human/57.jpg",
    "name": "Dr. Emma Brown",
    "speciality": {
      "icon": "faTooth",
      "title": "Dental Care"
    }
  },
  {
    "about": "Dr. Smith has extensive experience in treating musculoskeletal issues and focuses on minimally invasive techniques.",
    "address": {
      "line1": "1 Recovery Rd",
      "line2": "Room 305"
    },
    "available":True,
    "degree": "MBBS, MS (Ortho)",
    "experience": "10 Years",
    "fees": 100,
    "id": 4,
    "image": "https://mighty.tools/mockmind-api/content/human/5.jpg",
    "name": "Dr. John Smith",
    "speciality": {
      "icon": "faBrain",
      "title": "Neurology"
    }
  },
  {
    "about": "Dr. Grey is passionate about children's health, providing preventive care and treatment for young patients.",
    "address": {
      "line1": "76 Kids Care Lane",
      "line2": ""
    },
    "available": True,
    "degree": "MBBS, MD (Pediatrics)",
    "experience": "7 Years",
    "fees": 55,
    "id": 5,
    "image": "https://mighty.tools/mockmind-api/content/human/7.jpg",
    "name": "Dr. Alice Grey",
    "speciality": {
      "icon": "faEye",
      "title": "Eye Care"
    }
  },
  {
    "about": "Dr. Lee specializes in neurological disorders and is dedicated to comprehensive patient care.",
    "address": {
      "line1": "123 Neuro Street",
      "line2": "Suite 45"
    },
    "available": True,
    "degree": "MD, Neurology",
    "experience": "12 Years",
    "fees": 120,
    "id": 6,
    "image": "https://mighty.tools/mockmind-api/content/human/68.jpg",
    "name": "Dr. Kevin Lee",
    "speciality": {
      "icon": "faHeartPulse",
      "title": "Cardiology"
    }
  },
  {
    "about": "Dr. Ray provides expert care in eye health, focusing on both treatment and preventive measures.",
    "address": {
      "line1": "88 Vision Road",
      "line2": "Office 101"
    },
    "available": False,
    "degree": "MBBS, MD (Ophthalmology)",
    "experience": "9 Years",
    "fees": 70,
    "id": 7,
    "image": "https://mighty.tools/mockmind-api/content/human/60.jpg",
    "name": "Dr. Lisa Ray",
    "speciality": {
      "icon": "faEye",
      "title": "Eye Care"
    }
  },
  {
    "about": "Dr. Liu treats hormonal imbalances and is committed to helping patients achieve a balanced life.",
    "address": {
      "line1": "3 Wellness Ave",
      "line2": "Building B"
    },
    "available": True,
    "degree": "MD, Endocrinology",
    "experience": "5 Years",
    "fees": 80,
    "id": 8,
    "image": "https://mighty.tools/mockmind-api/content/human/49.jpg",
    "name": "Dr. Mark Liu",
    "speciality": {
      "icon": "faUserMd",
      "title": "Urology"
    }
  },
  {
    "about": "Dr. Williams is dedicated to women's health, providing a range of treatments and preventive care.",
    "address": {
      "line1": "200 Women's Health Road",
      "line2": "Floor 3"
    },
    "available": True,
    "degree": "MBBS, MD (Gynecology)",
    "experience": "11 Years",
    "fees": 90,
    "id": 9,
    "image": "https://mighty.tools/mockmind-api/content/human/43.jpg",
    "name": "Dr. Nora Williams",
    "speciality": {
      "icon": "faBrain",
      "title": "Neurology"
    }
  },
  {
    "about": "Dr. King specializes in cancer treatment, offering personalized care and comprehensive support.",
    "address": {
      "line1": "500 Hope Blvd",
      "line2": "Room 21A"
    },
    "available": False,
    "degree": "MD, Oncology",
    "experience": "15 Years",
    "fees": 150,
    "id": 10,
    "image": "https://mighty.tools/mockmind-api/content/human/41.jpg",
    "name": "Dr. Robert King",
    "speciality": {
      "icon": "faSyringe",
      "title": "Plastic Surgery"
    }
  }
]



@app.get('/doctors')
def get_doctors():
  return doctors_data
  