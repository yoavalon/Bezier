d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
