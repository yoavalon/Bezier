d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.S, Length.medium)

d.end()
