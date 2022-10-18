d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.long)

d.end()
