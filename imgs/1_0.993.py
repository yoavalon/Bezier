d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
