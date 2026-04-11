/**
 * This script simulates a spaced repetition system (like Anki) in a Google Sheet.
 * When a "Score" is entered for a topic, it automatically updates the review
 * schedule based on performance.
 *
 * @param {Object} e The event object from the onEdit trigger.
 */
function onEdit(e) {
  const sheet = e.source.getActiveSheet();
  const sheetName = sheet.getName();
  const DATE_FORMAT = "dd-MM-yyyy";

  // Only run the script on the specified sheets
  if (sheetName === "Neetcode 150[ANKI]" || sheetName === "Foundation") {
    const range = e.range;
    const row = range.getRow();
    const col = range.getColumn();

    // Get column indices from headers (row 1) to make the script more robust
    const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    const lastReviewedCol = headers.indexOf("Last Reviewed") + 1;
    const nextReviewCol = headers.indexOf("Next Review") + 1;
    const intervalCol = headers.indexOf("Interval") + 1;
    const easeCol = headers.indexOf("Ease") + 1;
    const scoreCol = headers.indexOf("Score") + 1;
    const reviewsCol = headers.indexOf("Reviews") + 1;
    const historyCol = headers.indexOf("History") + 1;

    // Check if the edited cell is in the "Score" column and not the header row
    if (col === scoreCol && row > 1) {
      const score = sheet.getRange(row, scoreCol);
      const scoreValue = score.getValue();

      // Skip processing if the score is empty to prevent errors
      if (scoreValue === "") return;

      const lastReviewed = sheet.getRange(row, lastReviewedCol);
      const interval = sheet.getRange(row, intervalCol);
      const ease = sheet.getRange(row, easeCol);
      const reviewCount = sheet.getRange(row, reviewsCol);
      const history = sheet.getRange(row, historyCol);

      // Initialize default values for new cards
      if (interval.isBlank()) interval.setValue(1);
      if (ease.isBlank()) ease.setValue(2.5); // Standard starting ease is 250%
      if (reviewCount.isBlank()) reviewCount.setValue(0);
      if (history.isBlank()) history.setValue("");

      // Update Last Reviewed Date to today
      lastReviewed.setValue(Utilities.formatDate(new Date(), Session.getScriptTimeZone(), DATE_FORMAT));

      // Update Interval and Ease Factor based on score
      let newInterval = interval.getValue();
      let newEase = ease.getValue();

      if (scoreValue === 0 || scoreValue === -1) { // Again
        newInterval = 1; // Reset interval
        newEase -= 0.2;
      } else if (scoreValue === 1 || scoreValue === 11) { // Hard
        newInterval *= 1.2;
        newEase -= 0.15;
      } else if (scoreValue === 2 || scoreValue === 22) { // Good
        newInterval *= newEase;
      } else if (scoreValue === 3 || scoreValue === 33) { // Easy
        newInterval *= newEase * 1.3;
        newEase += 0.15;
      }

      // --- Enforce a minimum ease factor ---
      // This prevents the ease from dropping too low, which would shrink future intervals.
      // 1.3 (or 130%) is the standard minimum in Anki.
      newEase = Math.max(1.3, newEase);

      // --- Round the interval and enforce a minimum of 1 day ---
      // This is the main fix. We round to the nearest whole day and ensure the
      // result is never less than 1, guaranteeing the next review is always tomorrow or later.
      newInterval = Math.max(1, Math.round(newInterval));
      
      interval.setValue(newInterval);
      ease.setValue(newEase);

      // Update Review Count
      reviewCount.setValue(reviewCount.getValue() + 1);

      // Update History log in reverse
      const formattedDate = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), DATE_FORMAT);
      const newHistoryEntry = `${formattedDate}(${scoreValue})`;
      history.setValue(history.getValue() ? `${newHistoryEntry}; ${history.getValue()}` : newHistoryEntry);

      // Calculate and update the Next Review Date
      const nextReviewDate = new Date();
      nextReviewDate.setDate(nextReviewDate.getDate() + newInterval);
      sheet.getRange(row, nextReviewCol).setValue(Utilities.formatDate(nextReviewDate, Session.getScriptTimeZone(), DATE_FORMAT));
      
      // Clear the score cell so it can be triggered again with the same number
      // score.clearContent();
    }
  }
}

