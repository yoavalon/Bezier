d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.W, Length.medium)

d.end()
