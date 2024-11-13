from keep_alive import keep_alive
from src.monitors.email_monitor import EmailMonitor
from src.config import load_config
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Load configuration
        config = load_config()
        
        # Initialize monitor
        monitor = EmailMonitor(config)
        
        # Start the Flask server in background
        keep_alive()
        
        # Start monitoring (this will run indefinitely)
        monitor.start_monitoring()
        
    except Exception as e:
        logger.error(f"Application failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
