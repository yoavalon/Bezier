d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
