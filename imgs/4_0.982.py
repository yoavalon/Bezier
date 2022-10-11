d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.position_pen(2,0)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SE, Length.long)

d.end()
