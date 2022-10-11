d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.SW, Length.long)

d.end()
