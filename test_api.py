import requests

def test_api_endpoints():
    print("Starting Automated API Security and Functional Test Suite...")
    
    # Target standard mock API for testing
    base_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Test Case 1: Validate GET Request (Functional & Response Code 200)
    response = requests.get(base_url)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    print("PASSED: GET Endpoint returned 200 OK.")
    
    # Test Case 2: Validate Security Headers (Basic Vulnerability Check)
    # Checking for missing standard security headers like Content-Type
    headers = response.headers
    assert "Content-Type" in headers, "FAIL: Missing Content-Type header!"
    assert "application/json" in headers["Content-Type"], "FAIL: Response is not JSON format"
    print("PASSED: Response headers and data format verified successfully.")
    
    # Test Case 3: Validate POST Request (Data Integrity Check)
    payload = {
        "title": "QA Security Test",
        "body": "Verifying input sanitization and secure endpoint transmission.",
        "userId": 1
    }
    post_response = requests.post(base_url, json=payload)
    assert post_response.status_code == 201, f"Expected 201 Created, but got {post_response.status_code}"
    
    # Verify the payload echoed back correctly
    data = post_response.json()
    assert data["title"] == payload["title"], "FAIL: Data corruption detected in transmission"
    print("PASSED: POST Endpoint validated with payload data integrity.")
    
    print("\n[SUCCESS] All API automated test cases passed flawlessly.")

if __name__ == "__main__":
    test_api_endpoints()
