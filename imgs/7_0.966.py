d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)

d.end()
