d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)

d.end()
